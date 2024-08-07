from django.urls import path
from . import views

app_name = 'todos'

# url namespace
# url을 이름으로 분류하는 기능
urlpatterns = [
    path('', views.index, name='index'),    # R
    path('create/', views.create, name='create'),   # C
    path('delete/<int:pk>', views.delete, name='delete'),   # D
    path('update/<int:pk>', views.update, name='update'),   # U
]