from django.forms import ModelForm
from .models import Article, Comment


class ArticleForm(ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']


class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']