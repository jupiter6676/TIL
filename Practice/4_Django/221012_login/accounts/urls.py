from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),    # 회원가입 페이지
    path('signup_complete/', views.signup_complete, name='signup_complete'),    # 회원가입 완료 페이지
    path('login/', views.login, name='login'),  # 로그인 페이지
    path('<int:pk>', views.detail, name='detail'),  # 회원 정보 조회 페이지
    path('logout/', views.logout, name='logout'),  # 로그아웃
]
