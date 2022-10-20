from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ['last_name', 'first_name', 'email']


class ProfileForm(ModelForm):

    class Meta:
        model = Profile()
        fields = ['nickname', 'intro', 'image']