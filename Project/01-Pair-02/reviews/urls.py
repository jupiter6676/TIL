from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path("", views.index, name="index"),
    path("movie_register/", views.movie_register, name="movie_register"),  # 관리자 영화 등록
    path("<int:movie_pk>", views.detail, name="detail"),  # 영화 상세 페이지
    path("<int:movie_pk>/create/", views.create, name="create"),  # 리뷰 작성 페이지
    path("<int:review_pk>/review_detail", views.review_detail, name="review_detail"),  # 리뷰 상세보기 페이지
    path("<int:review_pk>/delete", views.delete, name="delete"),  # 리뷰 삭제
    path("<int:review_pk>/review_edit", views.edit, name="edit"),  # 리뷰 수정
    path("search/", views.search, name="search"),  # 영화 검색
]
