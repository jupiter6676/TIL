# 1. aria

- 접근 가능한 리치 인터넷 어플리케이션
- 접근성과 관련되어 있다.



# 2. Bootstrap Grid System

## (1) Grid

- 요소들의 디자인과 배치에 도움을 주는 시스템
- 기본 요소
  - Column: 실제 콘텐츠를 포함하는 부분
  - Gutter: 칼럼과 칼럼 사이의 공간 (사이 간격)
  - Container: 칼럼들을 담고 있는 공간
- 12 Column Grid, 16 Column Grid를 주로 사용한다.
  - 약수가 많아야 배치를 다양하게 할 수 있기 때문이다.



## (2) Bootstrap Grid System

- Bootstrap Grid System은 **flexbox**로 제작되어 있다.
- **container**, **rows**, **column**으로 콘텐츠를 배치하고 정렬한다.
- 반드시 기억해야 할 2가지
  - **12개의 columns**
  - 6개의 grid breakpoints (화면의 너비에 따라 배치가 달라지는 분기점)

- 총 6개를 배치할 때

  - 한 줄에 가장 작은 화면은 1개, 모바일은 2개, 태블릿은 3개, PC은 4개를 배치하려면?

    ```html
    <div class="row my-3">
        <!-- 이걸 6번 반복 -->
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <div class="box">Box</div>
        </div>
    </div>
    ```



# 3. Media Query

- CSS에서 어떤 스타일을 선택적으로 적용하고 싶을 때 사용한다. if 조건문과 비슷한 개념이다.

  ```css
  @media (조건) {
      스타일;
  }
  ```

- 주로 뷰포트 너비에 따라 다양하게 콘텐츠를 배치하고 싶을 때, 미디어 쿼리를 직접 작성해서 쓴다.

