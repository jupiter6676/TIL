from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm # 회원가입, 정보 수정
from django.contrib.auth.forms import AuthenticationForm    # 로그인
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
# 회원 목록 조회 페이지
def index(request):
    return render(request, 'accounts/index.html')


# 회원 가입 페이지
def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = CustomUserCreationForm()
        
    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


# 로그인 페이지
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'index')

    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


# 로그아웃
def logout(request):
    if not request.user.is_authenticated:
        return redirect('index')

    auth_logout(request)

    return redirect('index')