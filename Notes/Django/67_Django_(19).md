# 1. Element.insertAdjacentHTML()

- innerHTML은 보안 문제가 있었는데

```js
comments.insertAdjacentHTML('afterend', `
	<p> ${response.data.userName} | ${reponse.data.content} </p>
	<hr>
`)
```

- JS에서 DOM 조작이 너무 어려워. 한땀한땀..
- Data가 변하면, Dom이 알아서 변할 수는 없을까?
  - React/Vue
- 한 서비스는 웹, IOS, Android 등 각 클라이언트마다 다른 언어로 서비스된다.
  - 서버는 JSON만 내뱉고, 각자 언어에 맞춰서 알아서 그리자!



# 2. Django query 심화

- articles = Article.objects 뒤에 붙일 수 있는 거



## (1) 댓글 수

- {% for article in articles %}
- article.comment_set.count
- `.annotate(Count('authors'))`
  - 요약된 값을 각각의 쿼리셋에 붙이고 싶을 때
  - ex) 책 목록을 가지고 오는데, 작가가 몇 명인지 알고 싶을 때가 있다면?
    - `.annotate(Count('authors'))`
- `.aggregate(Avg('price'))`: price 모델의 전체적인 평균



## (2) 작성자 이름

- {% for article in articles %}
- article.user.username과 article.title (JOIN)
- `.select_related('user')`
  - 유저의 정보를 한 번에 가져와서, 이 안에서 유저 정보를 찾으면 되기 때문에
  - 쿼리를 중복으로 여러 번 날리지 않고, 한 번만 날려도 된다.
  - one-to-one
- N + 1 쿼리 문제
  - 1개의 쿼리를 가지고 왔는데, 그걸 얻기 위해 N번의 쿼리를 더 날려야 하는 것



## (3) 댓글 목록

- article.comment_set.all
- `prefetch_related()`
  - 역참조 관계에서 사용하는 것 (JOIN X)
  - `prefetch_related('comment_set')`
  - many-to-many, many-to-one



## (4) 댓글 목록 ②

- {% for article in articles %}

- {% for comment in article.comment_set.all %}

- comment.contetnt (여기까진 OK)

- comment.user.username (여기서 중복)

- ```python
  articles = Article.objects.prefetch_related(
  	Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
  ).order_by('-pk')
  ```

