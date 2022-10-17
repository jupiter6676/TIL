# 1. 이미지 업로드 (기본 설정)

## (1) 미디어 파일

- 사용자가 웹에서 업로드하는 정적 파일 (User-uploaded)
- 유저가 업로드한 모든 정적 파일



## (2) Media 관련 필드

- `ImageField`
  - 이미지 업로드에 사용하는 모델 필드
  - `FileField`를 상속 받는 서브 클래스
    - FileField의 모든 속성 및 메소드를 사용 가능하다.
    - 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사한다.
  - ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경 할 수 있다.
  - [주의] 사용하려면 반드시 Pillow 라이브러리가 필요하다.
- `FileField`
  - 파일 업로드에 사용하는 모델 필드
  - 2개의 선택 인자를 가지고 있다.
    - `upload_to`, `storage`



## (3) 모델 설정

- `upload_to` argument

  - 문자열 경로 지정 방식

    ```python
    # models.py
    
    class MyModel(models.Model):
        # 1. MEDIA_ROOT/uploads/ 경로로 파일 업로드
        upload = model.FileField(upload_to='uploads/')
        
        # 혹은,
        # 2. MEDIA_ROOT/uploads/2022/01/01 경로로 파일 업로드
        upload = model.FileField(upload_to='uploads/%Y/%m/%d/')
    ```

  - 함수 호출

    ```python
    # models.py
    
    def articles_image_path(instance, filename):
        # MEDIA_ROOT/user_<pk>/ 경로에, <filename> 이름으로 업로드
        return f'user_{instance.user.pk}/{filename}'
    
    class Article(models.Model):
        image = models.ImageField(upload_to=articles_image_path)
    ```



## (4) URL 설정

- settings.py에 `MEDIA_ROOT`, `MEDIA_URL` 설정한다.

- `upload_to` 속성을 정의하여 업로드 된 파일에 사용할 `MEDIA_ROOT`의 하위 경로를 지정한다.

- 업로드 된 파일의 경로는 Django가 제공하는 'url' 속성을 통해 얻을 수 있다.

  ```html
  <img src="{{ article.image.url }}" alt="{{ article.image }}">
  ```



- `MEDIA_ROOT`

  ```python
  # settings.py
  
  MEDIA_ROOT = BASE_DIR/'media'
  ```

  - 사용자가 업로드한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로
  - Django는 성능을 위해, 업로드 파일은 데이터베이스에 저장하지 않는다.
  - 실제 DB에 저장되는 것은 파일의 경로

- `MEDIA_URL`

  ```python
  # settings.py
  
  MEDIA_URL = '/media/'
  ```

  - `MEDIA_ROOT`에서 제공되는 미디어를 처리하는 URL
  - 업로드 된 파일의 주소(URL)을 만들어 주는 역할
    - 웹 서버 사용자가 사용하는 public URL
  - 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 한다.



- 개발 단계에서 사용자가 업로드 한 파일 제공하기

  ```python
  # {project}/urls.py
  
  from django.conf.urls.static import static
  
  urlpatterns = {
      # ...
  } + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
  # 업로드 된 파일의 URL = settings.MEDIA_URL
  # 위 URL을 통해 참조하는 파일의 실제 위치 = settings.MEDIA_ROOT
  ```

  - 사용자가 업로드 한 파일이 우리 프로젝트에 업로드 되지만,
  - 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요하다.



# 2. 이미지 업로드 (CREATE)

## (1) Model 설정

- `ImageField`

  ```python
  # articles/models.py
  
  class Article(models.Model):
      # title, content, created_at, updated_at
      image = models.ImageField(blank=True, upload_to='images/')
  ```

  - `upload_to='images/'`: 실제 이미지가 저장되는 경로를 지정
  - `blank=True`: 이미지 필드에 빈 값(빈 문자열)이 허용되도록 설정 (이미지를 선택적으로 업로드)



- Model Field의 옵션 '**blank**'
  - 기본 값: False
  - True인 경우 필드를 비워둘 수 있고, DB에는 빈 문자열이 저장된다.
  - 유효성 검사에서 사용된다.
  - form에서 빈 값을 허용하려면 blank=True를 설정해야 한다.
- Model Field의 옵션 'NULL'
  - 기본 값: False
  - True인 경우, DB에는 NULL이 저장된다.
  - 주의 사항
    - CharField, TextField와 같은 문자열 기반 필드에서는 사용하면 X
    - 문자열 기반 필드에 True로 설정 시, '데이터 없음(no data)'은 '빈 문자열(1)'과 'NULL(2)'의 2가지 가능한 값이 있음을 의미하게 된다.
    - Django는 NULL이 아닌 빈 문자열을 사용하는 것이 규칙이다.



- 마이그레이션

  - 단, ImageField를 사용하기 위해서는 Pillow 라이브러리 설치가 필요하다.

    ```bash
    $ pip install Pillow
    $ pip python manage.py makemigrations
    $ pip python manage.py migrate
    ```



## (2) HTML 설정

- 게시글 작성 form enctype 속성 지정

  ```html
  <!-- articles/create.html -->
  
  <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="작성">
  </form>
  ```

- form 요소 `enctype(인코딩)` 속성

  - **`multipart/form-data`**
    - 파일/이미지 업로드 시에 반드시 사용해야 한다. (전송되는 데이터의 형식을 지정)
    - \<input type="file">을 사용할 경우에 사용
  - `application/x-www-form-urlencoded`
    - (기본값) 모든 문자 인코딩
  - `text/plain`
    - 인코딩을 하지 않은 문자 상태로 전송
    - 공백은 '+' 기호로 변환하지만, 특수 문자는 인코딩 하지 않는다.

- input 요소의 accept 속성 확인



## (3) View 설정

- 업로드한 파일은 `request.FILES` 객체로 전달된다.

  ```python
  # views.py
  
  @require_http_method(['GET', 'POST'])
  def create(request):
      form = ArticleForm(request.POST, request.FILES)
      
      # ...
  ```

- DB 및 파일 트리 확인: media/images/

- 실제 파일 위치: MEDIA_ROOT/images/



# 3. 이미지 업로드 (READ)

## (1) img 태그 활용

```html
<img src="{{ article.image.url }}" alt="{{ article.image }}">
```

- `article.image.url`: 업로드 파일의 경로
- `article.image`: 업로드 파일의 이름



# 4. 이미지 업로드 (UPDATE)

## (1) 이미지 수정하기

- 이미지는 바이너리 데이터(하나의 덩어리)이기 때문에,
- 텍스트처럼 일부만 수정하는 것은 불가능하고, 새로운 사진으로 덮어 씌우는 방식을 사용



## (2) HTML 설정

```html
<!-- articles/update.html -->

<form action="{% url 'articles:update' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="수정">
</form>
```



## (3) View 설정

```python
# views.py

@require_http_method(['GET', 'POST'])
def create(request):
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == 'POST':
    	form = ArticleForm(request.POST, request.FILES, instance=article)
    
    # ...
```



# 5. 이미지 Resizing

## (1) 개요

- 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업
- \<img> 태그에서 직접 사이즈를 조정할 수도 있지만(width 와 height), 업로드 될 때 이미지 자체를 resizing 하는 것을 사용해보자.
- django-imagekit 라이브러리 활용



## (2) Django-imagekit

- django-imagekit 설치 후 INSTALLED_APPS에 추가

  ```bash
  $ pip install django-imagekit
  ```

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      # ...
      'imagekit',
      # ...
  ]
  ```

- 이미지 크기 변경하기

  ```python
  # models.py
  
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  
  class Article(models.Model):
      # title, content, created_at, updated_at
      image = ProcessedImageField(
          upload_to='images/',
      	blank=True,
          processors=[Thumbnail(200, 300)],
          format='JPEG',
          options={'quality': 90}
      )
      
      def __str__(self):
          return self.title
  ```
  
  - ProcessedImageField()의 인자로 작성된 값들은 변경되더라도 다시 makemigrations를 해줄 필요 없이, 즉시 반영된다.



# 6. 기타

- Django Media
  - [Managing files | Django documentation | Django](https://docs.djangoproject.com/en/4.1/topics/files/)

- Django imagekit
  - https://github.com/matthewwithanm/django-imagekit

- [썸네일 만들기 (PILKit, imagekit) ImageSpecField, ProcessedImageField]
  - https://wayhome25.github.io/django/2017/05/11/image-thumbnail/

- Django Message Framework
  - [The messages framework | Django documentation | Django](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/)

- Django Widget Tweaks

  - https://pypi.org/project/django-widget-tweaks/

  - ModelForm의 username, label, errors를 분리할 수 있다.

    ```django
    {{ form.username }}
    {{ form.username.label }}
    {{ form.errors.username }}
    ```


  - widget tweaks로 bootstrap 커스텀하기

    ```django
    {% load widget_tweaks %}
    ```

    