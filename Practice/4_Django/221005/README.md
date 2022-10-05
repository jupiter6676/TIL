# 1.

1. 가상환경 설치 및 실행

2. django 3.2.13 버전 설치

3. django-bootstrap5 설치

4. django-admin startproject {pjt_crud} .

5. python manage.py startapp articles

6. `pjt_crud` 폴더 내 `settings.py`에 아래 코드 추가

   ```python
   INSTALLED_APPS = (
       # ...
       "articles",
       "django_bootstrap5",
       # ...
   )
   ```



# 2.

1. 최상위 폴더에 `templates` 폴더 생성 후, `base.html` 생성

2. `pjt_crud` 폴더 내 `settings.py`에 아래 코드 추가

   ```python
   TEMPLATES = [
       {
           # ...
           'DIRS': [BASE_DIR/'templates'],
           # ...
       },
   ]
   ```

3. `pjt_crud` 폴더 내 `urls.py`에 아래 코드 추가

   ```python
   urlpatterns = [
       # ...
       path('articles/', include('articles.urls')),
   ]
   ```

4. `articles` 폴더 내 `urls.py`에 index 경로 추가

   ```python
   from . import views
   
   app_name = 'articles'
   
   urlpatterns = [
       path('', views.index, name='index'),
   ]
   ```

5. `articles` 폴더 내 `views.py`에 index 함수 작성

   ```python
   def index(request):
       return render(request, 'articles/index.html')
   ```

6. `articles` 폴더 내 `templates/articles` 폴더 생성 후, `index.html` 작성

   → 누르면 글 작성 페이지(create.html)로 이동하는 버튼을 생성한다.

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>index</h1>
   
     <a href="{% url 'articles:create' %}" class="btn btn-primary">글 작성하기</a>
   {% endblock %}
   ```



# 3. Create (feat. ModelForm)

1. `articles` 폴더 내 `urls.py`에 create 경로 추가

   ```python
   urlpatterns = [
       # ...
       path('create/', views.create, name='create'),
   ]
   ```

2. `articles` 폴더 내 `views.py`에 create 함수 작성

   ```python
   def create(request):
       return render(request, 'articles/create.html')
   ```

3. `create.html` 생성

4. `articles` 폴더 내 `models.py` 파일에 다음과 같이 작성

   ```python
   class Article(models.Model):
       title = models.CharField(max_length=80)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

5. python manage.py makemigrations → python manage.py migrate

6. `articles` 폴더 내 `forms.py` 파일 생성 후 다음과 같이 작성

   ```python
   from django import forms
   from .models import Article
   
   class ArticleForm(forms.ModelForm):
       class Meta:
           model = Article
           field = '__all__'
   ```

7. `views.py`에 create 함수 작성

   ```python
   # 글 작성 페이지 (Create)
   def create(request):
       # 1. 사용자가 입력한 form data 받아오기
       # or None: ModelForm이 항상 에러 메시지를 띄우는 걸 방지
       form = ArticleForm(request.POST or None)
   
       # form data가 유효하면
       if form.is_valid():
           new_article = form.save()   # DB에 저장
   		
           # 세부 페이지를 아직 만들지 않았으므로, 우선은 메인 페이지로 이동
           return redirect('articles:index')
   
       # 2. 사용자가 입력할 form 양식을 템플릿에 보여주기
       context = {
           'form': form,
       }
   
       return render(request, 'articles/create.html', context)
   ```

8. `create.html` 파일 작성

   ```html
   {% extends 'base.html' %}
   {% load django_bootstrap5 %}
   
   {% block content %}
     <form action="{% url 'articles:create' %}" method="POST" class="form">
       {% csrf_token %}
       
       <!-- views에서 form을 가져와서 bootstrap 테마로 보여주기 -->
       {% bootstrap_form form %}
   
       {% bootstrap_button button_type="submit" content="완료" %}
       {% bootstrap_button button_type="reset" content="초기화" %}
     </form>
   {% endblock %}
   ```



# 4. Read

1. 

