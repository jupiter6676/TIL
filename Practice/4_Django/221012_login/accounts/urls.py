from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),    # 회원가입 페이지
    path('signup_complete/', views.signup_complete, name='signup_complete'),    # 회원가입 완료 페이지
    path('login/', views.login, name='login'),  # 로그인 페이지
]
