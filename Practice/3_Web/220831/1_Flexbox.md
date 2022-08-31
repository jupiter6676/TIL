# 1. Flexbox

> 1차원으로 항목 그룹을 배치하도록 설계된 레이아웃 메커니즘.

- 크가기 다른 여러 항목을 가져와서, 해당 항목에 가장 적합한 레이아웃을 반환하는 데 탁월
- 사이드바 패턴에 이상적인 레이아웃 모델
  - 사이드바와 콘텐츠를 인라인으로 배치하는 데 좋다.
  - 또한, 남은 공간이 충분하지 않은 경우 사이드바가 새 줄로 나뉜다.



## (1) 주 축과 교차 축

![나란히 있는 세 개의 상자, 왼쪽에서 오른쪽으로 가리키는 화살표가 존재하며 화살표에는 '주 축'이라는 표시가 있음. 위에서 아래로 향하고 있는 화살표가 하나 더 있으며 이것에는 '교차 축'이라는 표시가 있음.](https://web-dev.imgix.net/image/VbAJIREinuYvovrBzzvEyZOpw5w1/5wCsZcBmK5L33LS7nOmP.svg)

- 주 축 (Main axis)
  - `flex-direction` 속성으로 설정한 축
  - `flex-direction`
    - `row`인 경우 주 축은 행을 따른다.
    - `column`인 경우 주 축은 열을 따른다.

- 교차 축 (Cross axis)
  - 주 축과 다른 방향으로 설정된다.
  - 주 축의 `flex-direction`이 `row`이면, 교차 축은 열을 따라 실행된다.
  - 두 가지 작업 수행
    - 항목을 개별적으로, 또는 그룹으로 이동하여 정렬
    - flex line을 wrapping한 경우, 해당 라인의 공간 할당 방식을 제어



## (2) Flex Container 만들기

```html
<div class="container">
    <div>One</div>
    <div>Item tow</div>
    <div>The item we will refer to as three</div>
</div>
```

```css
.container {
    display: flex;
}
```

- flex container의 하위 항목은 즉시 flex 항목이 된다.
- 초기 값
  - `flex-direction: row;` → 항목이 행으로 표시된다.
  - `flex-wrap: nowrap;` → 요소가 강제로 한 줄에 배치된다.
  - 컨테이너를 채우기 위해 크기가 확대되지 않는다. (항목의 크기만큼 채워진다.)
  - 컨테이너의 시작 부분에 줄을 맞춘다.



## (3) 항목의 방향 제어

> flex-direction 속성

![위 용어의 레이블이 지정된 다이어그램](https://web-dev.imgix.net/image/VbAJIREinuYvovrBzzvEyZOpw5w1/uSH4TxRv8KNQDTK7Vn8h.svg)

- flex-directioin
  - `row`: 항목이 행으로 배치
  - `row-reverse`: 항목이 컨테이너의 끝부터 행으로 배치
  - `column`: 항목이 열로 배치
  - `column-reverse`: 항목이 컨테이너의 끝부터 열로 배치



- 항목 및 접근성의 흐름

  - `-reverse`는 접근성에 부정적 영향을 줄 수 있다.
  - 논리적 순서: 화면 읽기 프로그램이 내용을 읽고, 키보드를 사용하여 탐색하는 모든 사람이 따르는 순서
  - 이 논리적 순서가 아닌, 시각적 순서만 재정렬을 하기 때문에, 키보드 탐색에 부정적 영향을 줄 수 있다.

  <video src="https://storage.googleapis.com/web-dev-uploads/video/VbAJIREinuYvovrBzzvEyZOpw5w1/IgpaIRZd7kOq8sd46eaR.mp4"></video>

- 쓰기 모드와 방향
  - 우리의 쓰기 모드와, 문장이 진행되는 방향에 맞추어 행이 실행된다.
  - 만약 아랍어로 작업한다면,
    - 아랍어: 만약 오른쪽에서 왼쪽(RTL) 스크립트 방향을 가진다.
    - 항목이 오른쪽에 정렬되며, 탭 순서도 아랍어로 문장을 읽는 방식을 따르므로 오른쪽에서 시작한다.
  - 만약 일본어로 작업한다면,
    - 일부 세로 쓰기 모드로 작업하는 경우, 행은 위에서 아래로 실행된다.



## (4) 항목 래핑

> flex-wrap 속성

- `flex-wrap`
  - `nowrap`: 기본 값, 컨테이너에 공간이 충분하지 않으면 항목이 오버플로우된다.
  - `wrap`
    - 플렉스 컨테이너가 래핑되면, 여러 **Flex lines**이 생성된다.
    - 각 라인은 새로운 플렉스 컨테이너처럼 작동한다.
    - 따라서 행을 래핑하는 경우, 2행의 항목을 1행의 상위 항목과 정렬할 수 없다. (Grid는 가능)
    - 이것이 Flexbox가 1차원이라 불리는 이유이다.

- `flex-flow` 속성
  - `flex-direction` 및 `flex-wrap` 속성을 설정할 수 있다.



## (5) 항목 내부 공간 제어하기

> flex-grow, flex-shrink, flex-basis 속성

- `flex: inital;`
  - 컨테이너에, 항목을 표시하고도 남은 공간이 있다고 가정하자.
  - 그런 경우, 항목이 모두 배치된 후에도 남은 공간을 채우지 않는다.
  - 이걸 사용하면, 속성이 다음과 같이 설정된다. (기본 값)
    - `flex-grow: 0;` : 아이템이 확대되지 않는다.
    - `flex-shrink: 1;` : 항목이 `flex-basis`보다 작게 축소될 수 있다.
    - `flex-basis: auto;` : 항목의 기본 크기가 `auto`이다.
- `flex: auto;`
  - 큰 항목이 작은 항목보다 더 많은 공간을 가지도록 하는 동시에,
  - 항목이 확대되며 남는 공간을 채우도록 하기 위해 사용한다.
  - 이렇게 하면, 속성이 다음과 같이 설정된다.
    - `flex-grow: 1;` : 항목이 `flex-basis`보다 확대될 수 있다.
    - `flex-shrink: 1;` : 항목이 `flex-basis`보다 작게 축소될 수 있다.
    - `flex-basis: auto;` : 항목의 기본 크기가 `auto`이다.
  - 각 항목이 최대 콘텐츠 크기로 배치된 후, 남는 공간을 공유하므로 항목의 크기가 또 변한다.
  - 따라서 큰 항목은 더 많은 공간을 갖는다.
- `flex: 1;`
  - 항목의 콘텐츠 크기를 무시하고, 모든 항목을 일관된 크기로 만들기 위해 사용한다.
  - 이렇게 하면, 속성이 다음과 같이 설정된다.
    - `flex-grow: 1;` : 항목이 `flex-basis`보다 확대될 수 있다.
    - `flex-shrink: 1;` : 항목이 `flex-basis`보다 작게 축소될 수 있다.
    - `flex-basis: 0;` : 항목의 기본 크기가 `0`이다.
  - 모든 항목의 크기가 0이므로, 컨테이너의 모든 공간을 분배할 수 있다.
  - 모든 항목의 flex-grow 속성이 1이므로, 모두 동일한 크기로 확대되고, 공간을 동일하게 공유한다.
- `flex: none;`
  - 확대되거나 축소되지 않아 유연하지 않은 항목을 제공한다.
  - Flexbox만 사용하여 정렬 속성에 액세스하지만 유연한 동작을 원하지 않는 경우에 유용하다.



## (6) 항목이 다른 비율로 확대되도록 허용하기

> flex-grow 속성

- 플렉스 항목마다 flex-grow 인자를 다르게 지정할 수 있다.
- 만약 첫 번째 항목에 `flex: 1;`, 두 번째 항목에 `flex: 2;`, 세 번째 항목에 `flex: 3;`
  - 컨테이너의 총 가용 공간은 6개로 공유된다.
  - 첫 번째 항목은 한 칸, 두 번째 항목은 두 칸, 세 번째 항목은 세 칸이 제공된다.
- flex: {flex-grow} {flex-shrink} {flex-basis}



## (7) 항목 재정렬

> order 속성

- `order`
  - 서수 그룹의 항목 순서를 지정할 수 있다.
  - `flex-direction`이 지시하는 방향으로, 가장 낮은 값부터 먼저 항목이 배치된다.
- order를 사용하면, (3)에서와 같이 접근성 문제가 발생할 수 있다.
- 항목이 논리적으로 다른 순서로 있어야 하는 경우, HTML 코드를 수정한다.



## (8) Flexbox 정렬 개요

- 공간 분배 속성
  - `justify-content`: 주 축의 공간 분배
  - `alignment-content`: 교차 축의 공간 분배
    - 여러 줄들 사이의 간격을 지정한다.
    - 한 줄만 있는 경우, 효과를 보이지 않는다.
  - `place-content`: 위의 두 속성을 모두 설정하는 줄임 속성
- 정렬 속성
  - `align-self`: 교차 축에 단일 항목을 정렬
  - `align-items`: 모든 항목을 교차 축에 그룹으로 정렬
    - 컨테이너 안에서 어떻게 모든 요소들이 정렬하는지를 지정한다.



## (9) 주 축에 공간 분배하기

> justify-content 속성

- 항목은 플렉스 컨테이너를 완전히 채울만큼 크지 않다.
- `justify-content`
  - 주 축의 컨테이너에 여유 공간이 있어야 한다.
  - `flex-start`
    - 항목이 컨테이너 시작 부분에 정렬된다.
    - 남는 공간은 끝 부분에 정렬된다.
  - `flex-end`
    - 항목이 컨테이너 끝 부분에 정렬된다.
  - `space-between`
    - 항목 사이의 공간을 분배한다.
  - 그 외 `center`, `space-around`, `space-evenly`



- `flex-direction: column`
  - 주 축의 방향이 열이라면, `justify-content`가 해당 열에서 작동한다.
  - 열로 작업 시, 여유 공간을 확보하려면 컨테이너에 `height`나 `block-size`를 지정해야 한다.



## (10) 플렉스 라인 사이의 공간 분배

> align-content 속성

- 래핑된 플렉스 컨테이너
- `align-content`
  - `stretch`: 기본 값. 한 행의 항목이 최대 높이까지 늘어난다.
  - `flex-start`, `flex-start`, `center`, `space-between`, `space-around`, `space-evenly`

- `place-content`
  - `justify-content`와 `align-content`를 모두 설정



## (11) 교차 축에 항목 정렬하기

> align-itmes, align-self 속성

- 플렉스 라인 내에서, 교차 축에 대해 항목을 정렬한다.
- 정렬에 사용할 수 있는 공간은, 컨테이너의 높이에 따라 다르다.
- 래핑된 항목의 경우에는, 플렉스 라인에 따라 다르다.
- `align-self`
  - `stretch`: 기본 값. 한 행의 항목이 최대 높이까지 늘어난다.
  - `flex-start`, `flex-start`, `center`, `baseline`
- `align-items`
  - 래핑된 항목 전체에 대해 정렬
  - `stretch`, `flex-start`, `flex-start`, `center`, `baseline`



# 2. Flexbox Froggy

![image-20220831172210945](2_Flexbox-Froggy.png)
