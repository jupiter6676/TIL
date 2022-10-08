from django.shortcuts import render, redirect
from .models import Movie, Review
from .forms import MovieForm, ReviewForm

# Create your views here.
def index(request):
    contents = Movie.objects.all()
    context = {
        "contents": contents,
    }
    return render(request, "reviews/index.html", context)


def movie_register(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("reviews:index")
    else:
        movie_form = MovieForm()
    context = {
        "movie_form": movie_form,
    }
    return render(request, "reviews/register.html", context)


# 영화 상세 페이지
def detail(request, movie_pk):
    info = Movie.objects.get(pk=movie_pk)
    review = Review.objects.filter(movie_id=info.pk)
    context = {
        "info": info,
        "reviews": review,
    }
    return render(request, "reviews/detail.html", context)


# 리뷰 작성 페이지
def create(request, movie_pk):
    review_form = ReviewForm(request.POST or None)
    info = Movie.objects.get(pk=movie_pk)

    if review_form.is_valid():
        new = review_form.save(commit=False)
        new.movie_id = info.pk
        new.movie_name = info.title
        new.grade = len(new.star)
        new.save()
        return redirect("reviews:detail", info.pk)  # 나중에 댓글 상세보기 페이지로 이동

    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/create.html", context)


# 리뷰 삭제
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    movie_id = review.movie_id
    review.delete()
    return redirect("reviews:detail",movie_id)


def edit(request, review_pk):
    info = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=info)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:review_detail", info.pk)
    else:
        review_form = ReviewForm(instance=info)
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/review_edit.html", context)


def review_detail(request, review_pk):
    info = Review.objects.get(pk=review_pk)
    context = {
        "info": info,
    }
    return render(request, "reviews/review_detail.html", context)


def search(request):
    id = request.GET
    contents = Movie.objects.filter(title__contains=id["title"])
    context = {
        "contents": contents,
    }
    return render(request, "reviews/search.html", context)
