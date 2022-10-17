from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
import os


def index(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            new_article = form.save()
            return redirect('articles:detail', new_article.pk)

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)

    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }

    return render(request, 'articles/update.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)

    # 글 지우면, 사진을 서버에서도 지우기
    if article.image:
        os.remove(article.image.path)
    if article.thumbnail:
        os.remove(article.thumbnail.path)

    article.delete()

    return redirect('articles:index')