# 1. QnA

1. 같은 디테일 페이지안에서 댓글 수정 버튼을 누르면 댓글 수정은 댓글 각각 잘 되는데, 그 해당 댓글에만 폼이 나오는게 아니고 같은 유저가 여러 댓글을 쓰면 전부 다 폼이 다 나와요! 같은 페이지 내에서 제가 수정 버튼을 누른 메시지에만 폼을 보여주게 할 수는 없나요?
   - **댓글 수정은 JS**를 쓰는 것이 더 일반적이다.
   - (실제 커뮤니티들은 댓글 수정을 어떻게 구현하고 있지?)
     - 댓글 수정 버튼이나, 댓글 자체를 클릭
     - 기존 텍스트가 input으로 변경 (네이버 블로그)
     - 작성 후 확인하면, DB에 반영 후 적용
   - **같은 페이지에서 체류한 상태에서 비동기 처리**가 필요하다. (JS를 활용한 **ajax**)
   - 이걸 다음주에 할 예정
   - **axios** 라이브러리를 활용해서, 이벤트를 구현해보자.
   - 여기서 핵심은! 수정 이후에 JSON을 던져주어야 한다. 그리고 그 JSON을 받아서 한땀한땀



2. 참조와 역참조 중에 어떤 걸 선택해야 할지 헷갈린다. 쉽게 판단하는 방법이 있을까요?
   - ForeignKey를 어디에 넣어야 하는지 궁금한 거라면...
     - 댓글 기능을 예시로 할 때, Article과 Comment의 어디에 정의할까?
     - 모델이 뭐다? DB 구조. DB에 어떻게 넣을지를 생각하면 된다.
     - Article DB에서, 댓글 내용을 넣을까? 아니면 댓글 배열? 그런 건 본 적도 X
     - 그러면 반대로, Comment DB에 댓글 레코드를 기록해서, Article에서 FK로 댓글 id를 가져오는 식으로 한다.
   - comment_set을 써야 하는지, article_set을 써야 하는지 궁금한 거라면...
     - 어떤 구조로 설계했느냐에 따라 다르다.
     - comment.article →Article(1) : Comment(N)
     - user.article_set → User(1) : Article(N)



3. 배운 걸 응용해서 새 기능을 구현하고 싶은데 탐색할 시간이 적고, 만들어 둔 것에 덧붙이자니 이전에 학습한 유저 crud에도 게시판 crud만큼 익숙하지 않아 알던 것도 잊어버릴까 봐 걱정됩니다. 새로운 기능 구현을 시도 vs 배운 것을 100% 체득할때까지 계속 처음부터 만드는 연습
   - 인생은 전략이다.
   - 알던 것도 잊어버릴까 봐 → 인간은 망각의 동물
   - 내가 빠르게 리콜할 수 있어야 한다. 개념 지도와 정리를 틈틈이 하자.
   - 그리고 이 과정을 반복하면, 리콜이 빨라진다.



4. `request.user = user` / `comment.user = request`에서와 같은, request.user가 정확히 어떤 의미인지 알 수 있을까요? 템플릿에서 `request.user`와 `user`는 왜 같은 값이 출력되나요?
- user는 현재 로그인 된 사용자, request는 HttpRequest 객체인데,
   - request.user는 현재 로그인 된 사용자, 혹은 AnonymousUser이다.
- 즉, request.user와 user는 같은 것이다.



5. `request.user`는 로그인할 때 발생하고, `article.user`는 DB에서 가져오는데, 이 둘은 같은 객체인가요?
   - request는 HttpRequest object 그 자체 → 속성, 메소드가 있다.
   
     - request.user
       - 로그인 시 → User 객체 (로그인 한 사람)
       - 비로그인 시 → AnomynousUser 객체
   
     - article. user → User 객체 (게시글 쓴 사람)
   
     - comment.user → User 객체 (댓글 쓴 사람)
   
     - User.objects.get(pk=1) → User 객체 (pk가 1인 사람)
   
     - User.objects.all()[0] → User 객체 (User들 중에 첫 번째에 있는 사람)
   
     
   
   - 둘은 모두 User 클래스의 인스턴스인 건 맞다.
   
   - A로 로그인해서 B가 쓴 글을 보면, request.user는 A이고, article.user는 B이다.
   
   - 만약 둘이 같으면, 글의 수정, 삭제 버튼을 보여주기도 했다.



6. 저번 주 페어할 때 드라이버 바꾸고 pull하고 runserver 때마다 오류가 났는데, migrate로 해결이 됐어요. 이전 페어 때는 그런 오류가 없었는데, 어떤 게 잘못됐는지, 왜 migrate로 해결해야 하는지 궁금합니다.
   - git으로 주고받는 것은? 커밋
   - 커밋으로 안 담기는 파일은? `.gitignore`에 있는 것
   - 그러면 pull push에도 포함되지 않는다.
   - .gitignore에는? db.sqlite3가 있다. 그래서 서로 DB는 주고받지 못한다.
   - 그런데 makemigrations까지는 포함된다.
   - 그래서 다른 사람이 DB를 변경해도, pull 받으면 makemigrations 할 필요 없이 migrate만 하면 된다.
   - 정리
     - 모델/DB 변경점이 있다? → pull 받고 migrate 국룰
     - 패키지 추가 설치했다? → pull 받고 requirements.txt 설치



7. 모델 폼, 장고 폼쓰면 디자인이 어렵던데, 근데 is_valid 메소드를 쓰려면 모델폼을 써야하고.. 어떻게 해야할까요?
   - ModelForm → 출력할 때 쓰지 않고 그냥 valid 할 때만 써도 전혀 문제 없다.
   - 그런데 HTML Form, input 기본 요소를 다시 생각하자.
     - Form은 서버에 보내는 것(action, method)
     - input은 name 지정이 필수



8. comment모델을 만들고 commentForm을 장고폼으로 만들었는데 html에서 입력받아오는 양식을 장고폼이 아니라 제가 만든 일반폼으로 view함수로 넘겨줄 경우, commentForm(request.POST)로만 받아오면 실행이 되는 건가요?
   - 그냥 HTML Form을 써도 request.POST로 받아올 수 있다.



9. 한 모델 안에서 다른 모델의 어떠한 속성의 평균값을 정의하고 싶은데, models.py에서 사용할 수 있는 방법이 있을까요?

   - SQL 쿼리 했을 때를 떠올려보자.

   - 그냥 할 수 있다. models.py 안 쓰고 Django ORM으로도 가능하다.