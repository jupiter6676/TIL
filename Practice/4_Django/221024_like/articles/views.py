from urllib import request
from django.shortcuts import render, redirect
from .forms import CommentForm, ArticleForm
from .models import Article, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')

    # 페이지네이션
    page = request.GET.get('page', '1')
    paginator = Paginator(articles, 8)
    page_obj = paginator.get_page(page)

    context = {
        'articles' : articles,
        'question_list': page_obj,
    }
    
    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES)
        
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.save()
            return redirect('articles:index')
    
    else:
        form = ArticleForm()

    context = {
        'form' : form,
    }

    return render(request, 'articles/create.html', context)


# 리뷰 정보
def detail(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()

    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, 'articles/detail.html', context)


# 리뷰 수정
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.user != article.user:
        return redirect('articles:index')

    if request.method =='POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    
    else:
        article_form = ArticleForm(instance = article)

    context = {
        'article_form': article_form,
    }

    return render(request, 'articles/update.html', context)


# 리뷰 삭제
@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    
    if request.user != article.user:
        return redirect('articles:index')

    if article.image:
        os.remove(article.image.path)
    if article.thumbnail:
        os.remove(article.thumbnail.path)

    article.delete()
    

    # 회원 정보 페이지에서 삭제했으면
    if request.resolver_match.app_name == 'accounts':
        return redirect('accounts:detail', request.user.pk)
    
    # 글 페이지에서 삭제했으면
    else:
        return redirect('articles:index')


# 댓글 생성
@login_required
def create_comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()
    
    return redirect('articles:detail', article.pk)


# 댓글 삭제
@login_required
def delete_comment(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    if comment.user == request.user:
        comment.delete()
    
    # 회원 정보 페이지에서 삭제했으면
    # if request.resolver_match.app_name == 'accounts':
    #     return redirect('accounts:detail', request.user.pk)
    
    # # 글 페이지에서 삭제했으면
    # else:
    #     return redirect('articles:detail', article_pk)
    return redirect('articles:detail', article_pk)


# 검색
def search(request):
    search = request.GET.get('search')
    search_options = request.GET.get('Search_option')
    
    if search_options == 'movie_name__contains':
        articles = Article.objects.filter(movie_name__contains=search)
        
    elif search_options == 'title__contains':
        articles = Article.objects.filter(title__contains=search)

    page = request.GET.get('page', '1')
    paginator = Paginator(articles, 8)
    page_obj = paginator.get_page(page)

    context = {
        'question_list': page_obj,
        'search_options': search_options,
        'search': search
    }

    return render(request, 'articles/search.html', context)