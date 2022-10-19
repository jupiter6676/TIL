from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.user = request.user
            new_article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:detail', new_article.pk)

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    comment_form = CommentForm()
    comments = article.comment_set.all()

    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, 'articles/detail.html', context)


@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    # 글 작성자 == 로그인한 유저
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)

            if form.is_valid():
                form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('articles:detail', article_pk)

        else:
            form = ArticleForm(instance=article)

        context = {
            'article': article,
            'form': form,
        }

        return render(request, 'articles/update.html', context)

    # 글 작성자 != 로그인한 유저
    else:
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)


@login_required
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    # 글 작성자 == 로그인한 유저
    if article.user == request.user:
        # 글 지우면, 사진을 서버에서도 지우기
        if article.image:
            os.remove(article.image.path)
        if article.thumbnail:
            os.remove(article.thumbnail.path)

        article.delete()

    # 글 작성자 != 로그인한 유저
    else:
        messages.warning(request, '작성자만 삭제할 수 있습니다.')

    return redirect('articles:index')


# 댓글 생성
@login_required
def create_comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.article = article
        new_comment.user = request.user
        new_comment.save()

    return redirect('articles:detail', article.pk)


# 댓글 삭제
def delete_comment(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()

    return redirect('articles:detail', article_pk)