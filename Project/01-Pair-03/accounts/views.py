from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm  # 로그인
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }

    return render(request, "accounts/signup.html", context)


def login(request):
    # 사용자가 로그인했으면, 로그인을 할 수 없다.
    if request.user.is_authenticated:
        return redirect("accounts:index")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "accounts:index")

    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/login.html", context)


def logout(request):
    # 사용자가 로그인하지 않았으면, 로그아웃을 할 수 없다.
    if not request.user.is_authenticated:
        return redirect(request.GET.get("next") or "accounts:index")

    auth_logout(request)

    return redirect("accounts:index")


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user_": user,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def update(request, pk):
    user = get_user_model().objects.get(pk=pk)  # 수정할 대상

    # 로그인한 유저 != 수정할 정보를 가진 유저
    # 버튼은 막아뒀지만, url로 접근할 수 없도록 함.
    if request.user.pk != user.pk:
        return redirect(request.GET.get("next") or "reviews:index")

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)
