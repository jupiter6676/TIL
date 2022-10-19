from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth import get_user_model


# 회원가입
def signup(request):
    # 로그인 한 사용자는 회원가입 X
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            return redirect('articles:index')

    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


# 로그인
def login(request):
    # 로그인 한 사용자는 로그인 X
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, '로그인 하였습니다.')

            return redirect(request.GET.get('next') or 'articles:index')

    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


# 로그아웃
def logout(request):
    # 로그인 하지 않은 사용자는 로그아웃 X
    if not request.user.is_authenticated:
        return redirect('articles:index')

    auth_logout(request)
    messages.warning(request, '로그아웃 하였습니다.')

    return redirect('articles:index')


# 회원 조회 페이지 (작성한 게시글 목록)
def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    articles = user.article_set.all()

    context = {
        'user': user,
        'articles': articles,
    }

    return render(request, 'accounts/detail.html', context)