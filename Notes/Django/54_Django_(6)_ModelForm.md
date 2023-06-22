# 1. Django ModelForm

## (1) 개요

- DB 기반의 애플리케이션을 개발하다 보면, HTML Form(UI)은 Django의 모델(DB)과 매우 밀접한 관계를 가지게 된다.
  - 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문
  - 즉, 모델에 정의한 필드의 구성 및 종류에 따라 HTML Form이 결정된다.
- 사용자가 입력한 값이 DB의 데이터 형식과 일치하는지를 확인하는 유효성 검증이 반드시 필요하며, 이는 서버 사이드에서 처리해야 한다.



## (2) ModelForm Class

- Model을 통해 Form Class를 만들 수 있는 helper class
- ModelForm은 Form과 똑같은 방식으로 View 함수에서 사용

- ModelForm 선언

  - forms 라이브러리의 ModelForm 클래스를 상속받는다.

  - 정의한 ModelForm 클래스 안에 Meta 클래스를 선언한다.

  - 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정한다.

    ```python
    # articles/forms.py
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article	# Article 모델 기반
            fields = '__all__'
    ```



## (3) ModelForm에서의 Meta Class

- ModelForm의 정보를 작성하는 곳

- ModelForm을 사용할 경우 참조할 모델이 있어야 하는데, `Meta class`의 `model` 속성이 이를 구성한다.

  - 참조하는 모델에 정의된 field 정보를 Form에 적용한다.

    ```python
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ['title', 'content']
    ```

- `fields` 속성에 `__all__`을 사용하여, 모델의 모든 필드를 포함할 수 있다.

- 또는 `exclude` 속성을 사용하여, 모델에서 포함하지 않을 필드를 지정할 수 있다.

  ```python
  class Meta:
      model = Article
      exclude = ('title',)
  ```



## (4) ModelForm 활용

1. ModelForm 객체를 context로 전달

   ```python
   # articles/views.py
   from .forms import ArticleForm
   
   def new(request):
       form = ArticleForm()
       context = {
           'form': form,
       }
       
       return render(request, 'articles/new.html', context)
   ```



2. Input Field 활용

   ```html
   <!-- articles/new.html -->
   {% extends 'base.html' %}
   
   {% block content %}
   	<h1>New</h1>
   
       <form action="{% url 'articles:create' %}" method="POST">
           {% csrf_token %}
           {{ form.as_p }}
           <input type="submit">
       </form>
   	<a href="{% url 'articles:index' %}">[back]</a>
   {% endblock content %}
   ```



## (5) From rendering options

- `<label>` & `<input>` 쌍에 대한 3가지 출력 옵션
  - `as_p()`
    - 각 필드가 단락(`<p>` 태그)으로 감싸져서 렌더링
  - `as_ul()`
    - 각 필드가 목록 항목(`<li>` 태그)으로 감싸져서 렌더링
    - `<ul>` 태그는 직접 작성해야 한다.
  - `as_table()`
    - 각 필드가 테이블(`<table>` 태그) 행으로 감싸져서 렌더링



## (6) 저장 및 활용

```python
# articles/forms.py
from django import forms
from .models import Article

# form 클래스 생성
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article	# Article 모델 기반
        fields = '__all__'
```



```python
# articles.views.py
from .models import Article
from .forms import ArticleForm

# article을 추가하기 위한 form을 생성한다.
form = ArticleForm()

# 기존에 이미 있던 article을 수정하기 위한 form을 생성한다.
# instance를 지정하지 않으면 article이 수정되지 않고, 계속 새로 생성된다.
article = Article.objects.get(pk=1)
form = ArticleForm(instance=article)
```

```python
# articles.views.py
from .models import Article
from .forms import ArticleForm

# POST 데이터로부터 form 인스턴스를 만든다.
f = ArticleForm(request.POST)

# form 데이터를 Article 오브젝트로 저장한다.
new_article = f.save()

# 이미 존재하는 Article을 수정하기 위한 form을 생성한다.
# form을 수정할 때는 POST 데이터를 사용한다.
a = Article.objects.get(pk=1)
f = ArticleForm(request.POST, instance=a)
f.save()
```



# 2. ModelForm With View Functions

## (1) ModelForm 활용 로직

- 요청 방식에 따른 분기
  - HTML Form 전달
  - 사용자 입력 데이터 수신
- 유효성 검사에 따른 분기
  - 유효성 검사 실패 시, Form으로 전달
    - ex) Input 필드를 다 채우지 않은 경우, 해당 Form으로 Redirect
  - 유효성 검사 성공 시, DB에 저장



## (2) CREATE✨

```python
# articles/views.py
def create(request):
    form = ArticleForm(request.POST)
    
    # form이 유효하면
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    
    # form이 유효하지 않으면
    return redirect('articlese:new')
```

- 유효성 검사를 통과하면
  - 데이터 저장 후,
  - 상세 페이지로 리다이렉트
- 유효성 검사를 통과하지 못하면
  - 작성 페이지로 리다이렉트



## (3) Methods

- `is_valid()` 메소드

  - 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환한다.
  - 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해, Django는 `is_valid()`를 제공하여 개발자의 편의를 돕는다.

- `save()` 메소드

  ```python
  # CREATE
  form = ArticleForm(request.POST)
  form.save()
  
  # UPDATE
  form = ArticleForm(request.POST, instance=article)
  form.save()
  ```

  - form 인스턴스에 바인딩 된 데이터를 통해, 데이터베이스 객체를 만들고 저장한다.
  - ModelForm의 하위 클래스는 키워드 인자 instance 여부를 통해, 데이터를 생성할지 수정할지를 결정한다.
    - instance가 제공되지 않을 경우, `save()`는 지정된 모델의 새 인스턴스를 만든다. (CREATE)
    - instance가 제공될 경우, `save()`는 해당 인스턴스를 수정한다. (UPDATE)



## (4) form 인스턴스의 errors 속성

- `is_valid()`의 반환 값이 `False`인 경우, form 인스턴스의 `errors` 속성에 값이 작성된다.
- 유효성 검증을 실패한 원인이 딕셔너리 형태로 저장된다. → `form.errors`로 출력
- 유효성 검증을 실패했을 때 사용자에게 실패 결과 메시지를 출력해 줄 수 있다.



## (5) UPDATE✨

```python
# articles/views.py
def update(request, pk):	# edit()은 이제 필요 X
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/edit.html', context)
```

```html
<!-- articles/edit.html -->
{% extends 'base.html' %}
{% block content %}
    <h1>EDIT</h1>

    <form action="{% url 'articles:update' article.pk %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
    <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```

- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정한다.
- `request.POST`
  - 사용자가 form을 통해 전송한 데이터 (새로운 데이터)
- `instance`
  - 수정이 되는 대상
  - 없으면 CREATE



# 3. 정리

- Create: ① UI 제공(new), ② DB 저장(create) 

  → ModelForm: Model에 정의된 필드에 맞추어 ① UI를 그려주고, ② 유효성 검사를 해주고, ③ DB에 저장해준다.

- Read: ① DB에서 특정 게시글 가져와서 조회

- Delete: ① DB에서 특정 게시글 가져와서 삭제

- Update: ① UI 제공(edit), ② DB 저장(update) → ModelForm