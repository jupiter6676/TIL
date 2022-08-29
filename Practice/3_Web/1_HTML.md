# 1. HTML

## (1) HTML은 무엇인가?

- Hypertext Markup Language
  - **Hypertext**: 웹 페이지를 다른 페이지로 연결하는 링크
  - **Markup**
    - 웹 브라우저에 표시되는 글과 이미지 등의 다양한 콘텐츠를 표시하기 위한 것, 즉 콘텐츠 구조를 정의하는 언어이다.
    - `<head>`, `<title>`, `<body>` 등의 다양한 **요소**를 사용한다.

- 웹 콘텐츠의 의미와 구조를 정의할 때 사용
- HTML 이외의 기술
  - 웹 페이지의 모양/표현 (CSS)
  - 웹 페이지의 기능/동작 (JavaScript)



## (2) HTML의 요소

- 여는 태그와 닫는 태그: 요소의 시작과 끝을 나타낸다.
- 콘텐츠: 요소의 내용 (텍스트 등)
- 요소: 여는 태그 + 닫는 태그 + 콘텐츠
  - 요소는 중첩이 가능하고, 속성을 가질 수 있다.
  - 속성은 실제 콘텐츠로 표시되길 원하지 않는 추가적인 정보를 담고 있다.
  - <태그 속성="속성값">콘텐츠</태그>



## (3) HTML 문서 해부

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```

- `<!DOCTYPE html>`

  - doctype은 HTML이 막 나왔을 때, HTML 페이지가 따라야 할 일련의 규칙으로 작동하는 것을 의미하였다.
  - 하지만, 최근에는 신경 쓰지 않아도 되고, 그저 모든 것이 올바르게 동작하게 하기 위해 포함되어야 한다는 것만 알면 된다.

- `<html></html>`

  - 페이지 전체의 콘텐츠를 감싸며, 루트(root) 요소라고도 한다.

- `<head></head>`

  - HTML 페이지에 포함되어 있는 모든 것들 중, 사람들에게 보여지지 않을 콘텐츠의 컨테이너 역할을 한다.

  - 여기에는 **keywords**, 검색 결과에 표시되길 원하는 페이지 설명, 콘텐츠를 꾸미기 위한 CSS, 문자 집합 선언 등과 같은 것이 포함된다.

  - `<meta>`😉

    - 해당 문서에 대한 정보인 메타데이터를 정의할 때 사용
    - 언제나 `<head>` 요소 내부에 위치해야 한다.

    - name 속성이나http-equiv 속성이 명시되었다면, 반드시 content 속성도 함께 명시해야 한다.
    - HTML5에서는 `<meta>` 요소를 통해 웹 페이지에서 사용자가 볼 수 있는 영역인 뷰포트(viewport)를 제어할 수 있도록, name 속성에 viewport 속성값을 제공한다.
      - 원래 애플이 아이폰, 아이패드 등 모바일 브라우저의 뷰포트 크기 조절을 위해 만들었다.
      - 표준이 아니지만 다른 브라우저들도 이 태그를 채택하며 사실상 표준이 되었다.

  - `<meta>` 요소의 속성

    1. 검색 엔진을 위한 키워드(keyword)를 정의하는 예제

       ```html
       <meta name="keyword" content="HTML, meta, tag, element, reference">
       ```

    2. 웹 페이지에 대한 설명(description)을 정의하는 예제

       ```html
       <meta name="description" content="HTML meta tag page">
       ```

    3. 문서의 저자(author)를 정의하는 예제

       ```html
       <meta name="author" content="TCPSchool">
       ```

    4. 5초 뒤에 다른 페이지로 리다이렉트(redirect)시키는 예제

       ```html
       <meta http-equiv="refresh" content="5;url=http://www.tcpschool.com">
       ```

    5. 모든 장치에서 웹 사이트가 잘 보이도록 뷰포트(viewport)를 설정하는 예제

       ```html
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       ```

    6. 문자셋(charset)을 손쉽게 정의할 수 있는 속성 (HTML5)

       ```html
       <meta charset="UTF-8">
       ```

- `<body></body>`

  - 사람들에게 보여주기 원하는 모든 콘텐츠를 담고 있다.
  - 텍스트, 이미지, 비디오, 게임, 오디오 등

- `<meta charset="utf-8">`

  - 문서가 사용해야 할 문자 집합을 utf-8로 설정한다.
  - 본질적으로 우리가 사용할 수 있는 대부분의 문자 콘텐츠를 다룰 수 있다.

- `<title></title>`

  - 페이지의 제목을 설정하는 요소
  - 브라우저의 탭, 북마크, 즐겨찾기에 제목이 표시된다.



## (4) 이미지

> `<img>` 요소

```html
<img src="images/a.png" alt="My test image">
```

- `src` : 이미지 파일 경로를 포함하는 속성
- `alt` : 이미지를 볼 수 없는 사용자를 위한 설명문을 지정하는 속성
  - **시각 장애인**은 alt 텍스트를 읽어주는, 스크린 리더라는 도구를 사용한다.
  - 무언가 잘못되어 이미지를 표시할 수 없는 경우, 이미지의 위치에 alt 텍스트가 표시된다.



## (5) 문자 나타내기

1. 제목

   ```html
   <h1>My main title</h1>
   <h2>My top level heading</h2>
   <h3>My subheading</h3>
   <h4>My sub-subheading</h4>
   ```

   - 내용 특정 부분이 제목, 혹은 하위 제목임을 구체화
   - `<h1>` ~ `<h6>` 여섯 단계의 제목을 가지며, 3 ~ 4를 주로 사용한다.

2. 문단

   ```html
   <p>This is a single paragraph</p>
   ```

   - 문자의 문단을 포함하는 `<p>` 요소
   - 일반적 문자의 내용을 나타낼 때 많이 사용한다.

3. 목록

   ```html
   <ul>
     <li>technologists</li>
     <li>thinkers</li>
     <li>builders</li>
   </ul>
   
   <ol>
     <li>technologists</li>
     <li>thinkers</li>
     <li>builders</li>
   </ol>
   ```

   - 순서 없는 목록: `<ul>` 요소
   - 순서 있는 목록: `<ol>` 요소
   - 목록의 각 항목은 `<li>` 요소

4. 연결

   ```html
   <a href="https://google.com">google</a>
   ```

   - 문장 안의 어떠한 단어를 링크로 만들어 주는 `<a>` 요소
   - 문자를 `<a>` 요소로 감싸고, `href` 속성을 주고, 속성값으로 연결하기 원하는 웹 주소를 준다.



## (6) 인라인 요소 vs 블록 레벨 요소

- 인라인 요소

  - 콘텐츠의 흐름을 끊지 않고, 요소를 구성하는 태그에 할당된 공간만 차지한다.

  - 【예제 1】

    ```css
    .highlight {
        background-color: #ee3;
    }
    ```

    ```html
    <div>
        다음 span은 <span class="highlight">인라인 요소</span>로, 영향 범위의 시작과 끝을 알 수 있도록 배경색을 지정했습니다.
    </div>
    ```

    - `<div>`는 텍스트를 가진 블록 레벨 요소
    - 그 텍스트 안에는 인라인 요소인 `<span>`이 존재한다.
    - `<span>`은 인라인이기 때문에 전체 문단이 끊기지 않고 하나로 그려진다.

- 블록 레벨 요소

  - 부모 요소의 전체 공간을 차지하여 "블록"을 만든다.

  - 블록 레벨 요소는 인라인 요소와 다른 블록 레벨 요소를 포함할 수 있다.

  - 【예제 2】

    ```html
    <div>
        다음 p는 <p class="highlight">블록 레벨 요소</p>로, 영향 범위의 시작과 끝을 알 수 있도록 배경색을 지정했습니다.
    </div>
    ```

    - `<p>` 요소는 텍스트의 레이아웃을 완전히 바꿔, `<p>` 자기 자신의 텍스트, 그리고 `<p>` 이후의 세 부분으로 나눈다.



## (7) HTML 참고

- [HTML 요소 (Elements)](https://developer.mozilla.org/ko/docs/Web/HTML/Element)
- [HTML 속성 (Attributes)](https://developer.mozilla.org/ko/docs/Web/HTML/Attributes)
- [HTML 전역 특성 (Global attributes)](https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes)
- [HTML 표 (Table)](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics)
- [HTML 멀티미디어와 임베딩](https://developer.mozilla.org/ko/docs/Learn/HTML/Multimedia_and_embedding)
- [HTML 폼 가이드](https://developer.mozilla.org/ko/docs/Learn/Forms)



# 2. 출처

- [HTML: Hypertext Markup Language (mozilla)](https://developer.mozilla.org/ko/docs/Web/HTML)

- [HTML <meta> 태그 (TCPSchool)](http://www.tcpschool.com/html-tags/meta)