# 1. 마크다운

## 제목/소제목 (Heading)

#의 개수에 따라 h1 ~ h6까지 표현 가능하다.

### h3

#### h4

##### h5

###### h6



## 목록 (list)

### 순서가 없는 리스트: `-`(hypen), `*`(asterisk)

목록 활용 시 단계를 tab과 shift + tab으로 조절한다.

- 사과
- 바나나
  - 미니 바나나
  - Dole 바나나

- 딸기
  - 산딸기
- 복숭아
  - 백도 복숭아
  - 천도 복숭아



## 순서가 있는 리스트: `1.`

아침에 일어나서 KDT 교육 듣기

1. 세수하고 양치
2. 산책
3. Syllaverse 홈페이지에 접속한다.
   1. 로그인
   2. 대시보드 확인
4. 유튜브 라이브에 접속한다.
   1. 인사를 남긴다.



# Code Block (마크다운의 강점)

## Fenced Code Block

- `(backtick) 기호 3개를 활용하여 작성한다.
- 특정 언어를 명시하면 Syntax highlighting 기능이 적용된다.

```python
print("Hello")
# 주석

if True:
    print('t')
else:
    print('f')
```

```html
<h1>
    제목
</h1>
<!-- 주석 -->
```



## Inline Code Block

`print` 함수는 파이썬에서 출력하는 함수이다.



# 링크

대괄호에 글씨, 소괄호에 링크 (로컬 파일 주소도 O)

[깃허브](https://github.com/jupiter6676)

타이포라에서는 ctrl + click하면 창이 열린다.



# 이미지



마크다운.assets/aa.png는 상대경로, C:\Users\…는 절대경로

마크다운.asset과 마크다운.md 파일을 같이 보내면 이 이미지가 같이 보인다.

- 아래의 이미지는 나오지 않음

  - 절대경로

    ![aa](C:\Users\jupit\OneDrive\Desktop\aa.png)

- 아래의 이미지는 나옴
  - 상대경로
  - 01_1_Markdown.assets 폴더를 같이 공유

![aa](/Assets/01_1_Markdown.assets/aa.png)



# 인용문

> Life is short, you need python.



# 표

타이포라 기능을 적극 활용하자.

본문 → 표 → 표 삽입 (ctrl + t)

| 이름 | 댓글                               |
| ---- | ---------------------------------- |
| A    | 노션이랑 비슷하네요                |
| B    | 빨간색 노란색 프로그램 무엇인가요? |



# 텍스트

**굵게(볼드체)** : `**`

*기울임(이탤릭체)* : `*`

~~취소선~~ : `~~`



# 수평선

`---`

---



# ✨ 기타 정리

- 띄어쓰기 있는 것
  - 제목 (`#`)
  - 목록 (`-`, `1.`)
- 띄어쓰기 없는 것
  - `inline code block`, *기울임*, **굵게**, ***기울임 굵게***

- 예시: Technical Writing 등

