from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm   # 회원가입, ModelForm(UserCreationForm)
from django.contrib.auth.forms import AuthenticationForm    # 로그인, 일반 Form
from django.contrib.auth import login as auth_login # 로그인

# Create your views here.
def index(request):
    users = get_user_model().objects.all()

    context = {
        'users': users,
    }

    return render(request, 'accounts/index.html', context)


# 회원가입 폼 페이지
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            # auth_login(request, user)
            return redirect('accounts:signup_complete') # 회원가입 완료 페이지로 이동

    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


# 회원가입 완료 페이지
def signup_complete(request):
    return render(request, 'accounts/signup_complete.html')


# 로그인 페이지
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            # return redirect(request.GET.get('next') or 'index')
            return redirect('index')

    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


# 회원 정보 조회
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)

    context = {
        'user': user,
    }

    return render(request, 'accounts/detail.html', context)