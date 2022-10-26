from django.shortcuts import render,redirect, get_object_or_404
from .forms import SignupForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')

    else:
        form = SignupForm()

    context = {
        'form' : form,
    }

    return render(request,'accounts/signup.html',context)


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def logout(request):
    if not request.user.is_authenticated:
        return redirect('articles:index')

    auth_logout(request)

    return redirect('articles:index')


def detail(reqeust, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    articles = user.article_set.all()
    comments = user.comment_set.all()

    context = {
        'user': user,
        'articles': articles,
        'comments': comments,
    }

    return render(reqeust, 'accounts/detail.html', context)


@login_required
def update(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)

    if request.user != user:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('accounts:detail', user_pk)

    else:
        form = CustomUserChangeForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'accounts/update.html', context)


@login_required
def password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:detail', request.user.pk)
    
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form' : form,
    }
    
    return render(request, 'accounts/password.html', context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)

    return redirect('articles:index')


@login_required
def follow(request, user_pk):
    # user = get_user_model().objects.get(pk=user_pk)
    user = get_object_or_404(get_user_model(), pk=user_pk)

    # 스스로 팔로우 X
    if user == request.user:
        return redirect('accounts:detail', user_pk)

    # 이미 팔로우 중이라면, 팔로우 취소
    if user.followers.filter(pk=request.user.pk).exists():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)

    return redirect('accounts:detail', user_pk)