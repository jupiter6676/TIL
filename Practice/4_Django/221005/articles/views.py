from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# 메인 페이지 (글 목록)
def index(request):
    articles = Article.objects
    return render(request, 'articles/index.html')

# 글 작성 페이지 (Create)
def create(request):
    # 사용자가 입력한 form data 받아오기
    # or None: ModelForm이 항상 에러 메시지를 띄우는 걸 방지
    form = ArticleForm(request.POST or None)

    # form data가 유효하면
    if form.is_valid():
        new_article = form.save()   # DB에 저장

        return redirect('articles:index')
        # return redirect('reviews:detail', new_article.pk)   # 세부 페이지로 이동

    # 사용자가 입력할 form 양식을 템플릿에 보여주기
    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)