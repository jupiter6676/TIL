from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# 메인 페이지 (글 목록)
def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


# 글 작성 페이지 (Create)
def create(request):
    # 사용자가 입력한 form data 받아오기
    # or None: ModelForm이 항상 에러 메시지를 띄우는 걸 방지
    form = ArticleForm(request.POST or None)

    # form data가 유효하면
    if form.is_valid():
        new_article = form.save()   # DB에 저장
        return redirect('articles:detail', new_article.pk)   # 세부 페이지로 이동

    # 사용자가 입력할 form 양식을 템플릿에 보여주기
    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)


# 글 세부 페이지
def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


# 글 삭제
def delete(request, pk):
    Article.objects.get(pk=pk).delete()

    return redirect('articles:index')


# 글 수정 페이지
def update(request, pk):
    article = Article.objects.get(pk=pk)

    # 만약 사용자가 데이터를 새로 입력했다면,
    if request.method == 'POST':
        # 기존의 값을 새로운 값으로 변경한 form 데이터를 가져와서
        form = ArticleForm(request.POST, instance=article)

        # 유효한지 검사한 후,
        if form.is_valid():
            form.save() # DB에 저장하고
            return redirect('articles:detail', article.pk)  # 상세 페이지로 이동

    # 아직 글을 수정하지 않았다면
    else:
        # 기존의 값이 담긴 form 데이터를 가져오기
        form = ArticleForm(instance=article)
    
    # 사용자가 입력할 form 양식을 템플릿에 보여주기
    context = {
        'article': article,
        'form': form,
    }

    return render(request, 'articles/update.html', context)