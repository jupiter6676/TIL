from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'thumbnail']