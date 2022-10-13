from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm # 회원가입, 정보 수정
from django.contrib.auth.forms import AuthenticationForm    # 로그인
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required   # 회원 정보 수정

# Create your views here.
# 회원 목록 조회 페이지
def index(request):
    users = get_user_model().objects.all()

    context = {
        'users': users,
    }

    return render(request, 'accounts/index.html', context)


# 회원 가입 페이지
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('accounts:index')

    else:
        form = CustomUserCreationForm()
        
    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


# 로그인 페이지
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')

    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


# 로그아웃
def logout(request):
    if not request.user.is_authenticated:
        return redirect('accounts:index')

    auth_logout(request)

    return redirect('accounts:index')


# 회원 정보 조회 페이지
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)

    context = {
        'user': user,
    }

    return render(request, 'accounts/detail.html', context)


# 회원 정보 수정 페이지
@login_required
def update(request, pk):
    user = get_user_model().objects.get(pk=pk)

    # 로그인한 유저 != 수정할 정보를 가진 유저
    if request.user.pk != user.pk:
        return redirect(request.GET.get('next') or 'accounts:index')

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)

    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'accounts/update.html', context)