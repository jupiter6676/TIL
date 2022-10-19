# 1. 1:N (User-Comment)

## (1) 개요

- User(1) - Comment(N)
- User 모델과 Comment 모델 간 관계 설정
- "0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있다."



## (2) 모델 관계 설정

- Comment

  - id, content, created_at, updated_at, **User의 id**

- User

  - id, username, first_name, last_name, 기타

- Comment 모델에 User 모델을 참조하는 외래 키 작성

  ```python
  # articles/models.py
  
  class Comment(models.Model):
  	article = models.ForeignKey(Article, on_delete=models.CASCADE)
  	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      # ...
  ```



## (3) CREATE

- 인증된 회원의 댓글 작성 구현
- 작성하기 전, 로그인을 먼저 진행



- CommentForm

  - CommentForm 출력을 확인해보면, create 템플릿에서 불필요한 필드 user가 출력된다.
  - user 필드에 작성해야 하는 user 객체는 view 함수의 request 객체를 활용해서, 로그인 한 유저의 정보가 자동으로 입력되도록 해야 한다.

- CommentForm의 출력 필드 수정

  ```python
  # articles/forms.py
  
  class CommentForm(forms.ModelForm):
  	class Meta:
  		model = Comment
          exclude = ('article', 'user',)
  ```



- 외래 키 데이터 누락

- 댓글 작성 시, 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션을 활용

  ```python
  def comments_create(request, pk):
      
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm(request.POST)
      
      if comment_form.is_valid():
      	comment = comment_form.save(commit=False)
      	comment.article = article
      	comment.user = request.user
      	comment.save()
      
      return redirect('articles:detail', article.pk)
  ```



## (4) READ

- 댓글 작성자 출력

- detail 템플릿에서 각 게시글의 작성자 출력

  ```html
  {% for comment in comments %}
  	...
  	{{ comment.user }}
  	...
  {% endfor %}
  ```



## (5) DELETE

- 댓글 삭제 시 작성자 확인

- 이제 댓글에는 작성자 정보가 함께 들어있기 때문에, 

- 현재 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제 할 수 있도록 한다.

  ```python
  # articles/views.py
  
  def comments_delete(request, article_pk, comment_pk):
      comment = Comment.objects.get(pk=comment_pk)
      
      if request.user == comment.user:
      	comment.delete()
      
      return redirect('articles:detail', article_pk)
  ```

- 추가로 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 한다.

  ```html
  {% if request.user == comment.user %}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
      </form>
  {% endif %}
  ```





# 2. 기타

- user가 작성한 글 중, 처 번째 글의 댓글 중, 첫 번째 user
  - user.article_set.all[0].comment_set.all[0].user
- input을 마크다운으로
  - https://github.com/agusmakmun/django-markdown-editor