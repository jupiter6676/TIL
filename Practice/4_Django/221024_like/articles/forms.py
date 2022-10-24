from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        exclude = ('user',)
        labels = {
            'title': '제목',
            'content': '내용',
            'movie_name': '영화제목',
            'grade': '평점',
            'image': '사진',
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': '내용',
        }