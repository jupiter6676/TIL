from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/like/', views.like, name='like'),
    path('<int:review_pk>/comment/', views.comment_create,name='comment_create'),
    path('<int:review_pk>/comment/<int:comment_pk>/delete/', views.comment_delete,name='comment_delete'),
]
