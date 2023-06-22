# 1. 파이썬 응용/심화

## (1) List Comprehension

- 표현식과 제어문을 통해, 특정 값을 가진 리스트를 간결하게 생성하는 방법
  - [<expression> for <변수> in <iterable>]
  - [<expression> for <변수> in <iterable> if <조건식>]
- Dictionary Comprehension
  - {key: value for <변수> in <iterable>}
  - {key: value for <변수> in <iterable> if <조건식>}



## (2) Lambda

- `lambda [parameter] : <표현식>`
- 람다함수
  - 표현식을 계산한 결과값을 반환하는 함수
  - 이름이 없는 함수여서 익명함수라고도 불림
- 특징
  - return문을 가질 수 X
  - 간편 조건문 외 조건문이나, 반복문을 가질 수 X
- 장점
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능



- 【예시 1】 리스트의 모든 요소에 ×3 해보기

  ```python
  numbers = [1, 2, 5, 10, 3, 9, 12]
  ```

  ```python
  # 기존 반복/조건 코드
  res = list()
  for n in numbers:
      res.append(n)
  print(res)
  ```

  ```python
  # 함수 정의 → map
  def multiple_3(n):
      return n * 3
  print(list(map(multiple_3, numbers)))
  ```

  ```python
  # 그런데 multiple_3 함수는 계속 사용되지 않고, map에서만 사용된다.
  # 임시적인 함수를 만들자! → lambda
  print(list(map(lambda n: n*3, numbers)))
  ```



- 【예시 2】 3의 배수만 있는 리스트로 만들기

  - `filter()` 함수
    - `filter(<function>, <iterable>)`
    - 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환 (map 함수 생각)

  ```python
  numbers = [1, 2, 5, 10, 3, 9, 12]
  ```

  ```python
  # 함수 정의 → filter
  def is_3(n):
      return n % 3 == 0
  ```

  ```python
  # lambda
  print(list(filter(lambda n: n % 3 == 0, numbers)))
  ```



# 2. 파이썬 버전별 업데이트

- 하위 버전 호환성

- 파이썬 3.8 새 기능

  - 위치 전용 매개 변수

    ```python
    # a와 b는 위치 전용
    # c, d는 위치나 키워드
    # e, f는 키워드 전용
    def func(a, b, /, c, d, *, e, f)
    ```

    ```python
    # 유효한 호출
    func(10, 20, 30, d=40, e=50, f=60)
    ```

  - 변수 어노테이션(Annotation)

    - 동적 타입 언어인 파이썬에서,
    - 정적 타입 언어로 바꿔주는 게 아니라 그냥 힌트를 주는 것

    ```python
    # 변수 어노테이션
    a: int = 3
    print(a)
    ```

    ```python
    # 함수 어노테이션
    # x, y에 int가 꼭 오지 않아도 됨.
    # 그러나 힌트를 주는 효과
    def add(x: int, y: int) -> int:
        return x + y
    
    print(add(7, 4))	# 11
    print(add('hi', 'hello'))	# hi hello
    ```



# 3. 모듈 심화

- 다양한 패키지를 하나의 묶음으로 → library
- 이것을 관리하는 것 → pip (파이썬 패키지 관리자)



## (1) pip 명령어

- 패키지 설치

  - 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음.
  - 이미 설치되어 있는 경우, 아무것도 하지 않음.

  ```bash
  $ pip install SomePackage
  $ pip install SomePackage==1.0.5
  $ pip install 'SomePackage'>=1.0.5
  ```

- 패키지 삭제

  ```bash
  $ pip uninstall SomePackage
  ```

- 패키지 목록 및 특정 패키지 정보

  ```bash
  $ pip list
  $ pip show SomePackage
  ```

- 패키지 freeze

  - 설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용되는 형식으로 출력
  - 해당 목록을 requirements.txt (관습)으로 만들어 관리

  ```bash
  $ pip freeze
  ```

- **패키지 관리**

  - 아래의 명령어들을 통해 패키지 목록을 (1) 관리하고, (2) 설치할 수 있음
  - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함

  ```bash
  $ pip freeze > requirements.txt
  $ pip install –r requirements.txt
  ```



## (2) 가상환경

- 외부 패키지와 모듈을 사용하는 경우, 모두 pip를 통해 설치해야 함.
- **복수의 프로젝트를 하는 경우 버전이 상이**할 수 있음.
  - 과거 외주 프로젝트 – django 버전 2.x
  - 신규 회사 프로젝트 – django 버전 3.x
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리 할 수 있음.



## (3) venv

- 가상 환경을 만들고 관리하는데 사용되는 모듈 (Python 버전 3.5 ~)

- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음.
  - 특정 폴더에 가상 환경(패키지 집합 폴더 등)이 있고,
  - 실행 환경(예 – bash)에서 가상환경을 활성화시켜,
  - 해당 폴더에 있는 패키지를 관리/사용함.



- 가상환경 생성

  - 가상환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨.

  ```bash
  $ python -m venv <폴더명>
  ```

- 가상환경 실행(활성화)

  ```bash
  $ source <venv>/Scripts/activate
  ```

- 여러 프로젝트를 수행할 때, 각각 패키지 버전이 달라야 한다면, **각 프로젝트에 대해 별도의 venv 폴더를 만들어서 패키지 버전 관리**를 하게 된다.

- 즉, 동일 컴퓨터에서 별도의 가상환경을 구축할 수 있따.

  