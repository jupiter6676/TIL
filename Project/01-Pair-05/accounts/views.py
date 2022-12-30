from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.
def index(request):
    users = get_user_model().objects.all()

    print(users)

    context = {
        "users": users,
    }

    return render(request, "accounts/index.html", context)


def signup(request):
    if request.user.is_authenticated:
        return redirect("accounts:index")

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
    if request.user.is_authenticated:
        return redirect("accounts:index")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")

    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:index")


def detail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    context = {
        "user": user,
    }

    return render(request, "accounts/detail.html", context)


@login_required
def update(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    if request.user != user:
        return redirect("accounts:detail", user_pk)

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("accounts:detail", user_pk)

    else:
        form = CustomUserChangeForm(instance=user)

    context = {
        "form": form,
    }

    return render(request, "accounts/update.html", context)


def follow(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    if user == request.user:
        return redirect("accounts:detail", user_pk)

    if user.followers.filter(pk=request.user.pk).exists():
        user.followers.remove(request.user)
        is_followed = False
    else:
        user.followers.add(request.user)
        is_followed = True

    context = {
        "followers_count": user.followers.count(),
        "followings_count": user.followings.count(),
        "is_followed": is_followed,
    }

    return JsonResponse(context)
