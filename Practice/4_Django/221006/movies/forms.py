from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        labels = {
            'title': '제목',
            'running_time': '상영 시간',
            'summary': '줄거리',
        }

        # widgets = {
        #     'summary': forms.Textarea(attrs={'id': 'summary'})
        # }