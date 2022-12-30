from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
   class Meta(UserCreationForm.Meta): 
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
        labels = {
            'username':'닉네임',
            'password1': '비밀번호',
            'password2' : '비밀번호 확인'
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'last_name', 'first_name')
        labels = {
            'email' : '이메일',
            'last_name': '성',
            'first_name' : '이름'
        }