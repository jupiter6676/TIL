from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.

# 글 목록(게시판) 페이지
def index(request):
    posts = Review.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'reviews/index.html', context)


# 글 작성 후 DB에 저장
def create(request):
    form = ReviewForm(request.POST)

    if form.is_valid():
        post = form.save()  # DB에 저장

        # 글 세부 페이지로 이동
        return redirect('reviews:detail', post.pk)

    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)


# 리뷰 보기 페이지
def detail(request, pk):
    post = Review.objects.get(id=pk)

    # content_ = post.content.replace('<br>', '\r\n')

    context = {
        'id': post.pk,
        'title': post.title,
        'content': post.content.replace('<br>', '\r\n'),
    }

    return render(request, 'reviews/detail.html', context)


# 글 수정 후 DB 갱신
def update(request, pk):
    post = Review.objects.get(id=pk)

    # 만약 사용자가 새로 데이터를 입력했다면
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=post)

        # 유효성 검사 후
        if form.is_valid():
            form.save() # DB에 저장
            return redirect('reviews:detail', post.pk)  # 상세 페이지로 이동

    # request method가 GET이면
    # = 수정 페이지에 들어오기만 했다면
    else:
        form = ReviewForm(instance=post)    # 기존에 있던 글 가져오기
    
    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'reviews/update.html', context)


# 글 삭제 후 DB 갱신
def delete(request, pk):
    post = Review.objects.get(id=pk)
    post.delete()

    return redirect('reviews:index')