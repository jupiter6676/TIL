from django.shortcuts import render, redirect
from .forms import ReviewCreationForm
from .models import Review
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    reviews = Review.objects.order_by("-id")
    page = request.GET.get("page", "1")
    paginator = Paginator(reviews, 3)
    page_obj = paginator.get_page(page)
    context = {
        "reviews": reviews,
        "question_list": page_obj,
    }
    return render(request, "reviews/index.html", context)


@login_required
def create(request):
    # 로그인 하지 않으면 글 작성 X
    if not request.user.is_authenticated:
        return redirect(request.GET.get("next") or "reviews:index")

    if request.method == "POST":
        form = ReviewCreationForm(request.POST)

        if form.is_valid():
            new = form.save(commit=False)
            new.user_id = request.user.pk
            new.grade = len(new.star)
            new.save()
            return redirect("reviews:detail", new.pk)

    else:
        form = ReviewCreationForm()
        print(dir(form))

    context = {
        "form": form,
    }

    return render(request, "reviews/create.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)

    # 로그인 하지 않으면 글 수정 X
    # 글 작성자를 FK로 해서 그 사람만 수정할 수 있게 하면 좋을 것 같다.
    if not request.user.is_authenticated:
        return redirect(request.GET.get("next") or "reviews:index")

    if request.user.pk != review.user_id:
        return redirect(request.GET.get("next") or "reviews:index")
    
    if request.method == "POST":
        form = ReviewCreationForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("reviews:detail", pk)
    else:
        form = ReviewCreationForm(instance=review)
    context = {
        "form": form,
        "review": review,
    }
    return render(request, "reviews/update.html", context)


def delete(request, pk):
    review = Review.objects.get(pk=pk)

    if request.user.pk != review.user_id:
        return redirect(request.GET.get("next") or "reviews:index")

    review.delete()
    
    return redirect("reviews:index")
