# 0. 컴퓨터 프로그래밍 언어

- 컴퓨터 프로그래밍 언어의 정의

  - 컴퓨터: Calculation + Remember

  - 프로그래밍
    - 프로그램: 명령어의 집합

  - 언어
    - 자신의 생각을 나타내고 전달하기 위해 사용하는 체계
    - 문법적으로 맞는 말의 집합

  - 컴퓨터에게 명령어를 전하는 말

- 선언적 지식 vs 명령적 지식

  - 선언적 지식: 사실에 대한 내용

  - **명령적 지식**: How-to



# 1. 파이썬 개발 환경

## 1. 파이썬이란?

- Easy to Learn

  - 동적 타이핑 언어: 변수에 별도의 타입 지정이 필요 X
  - 문법이 간결, 엄격하지 X

- Expressive Language: C, Java 보다 간결

- 인터프리터 언어: 컴파일 없이 바로 실행

- ✨ **객체 지향 프로그래밍**

  - 모든 것이 객체로 구현

  - 객체: 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것을 의미

    그냥 파이썬에서 어떠한 것을 부를 때 객체라고 표현한다~



# 2. 기초 문법

## 1. 코드 스타일 가이드

- ✨ **PEP8**: 파이썬에서 제안하는 스타일 가이드
- Google Style Guide: 기업, 오픈소스 등에서 사용되는 스타일 가이드

```python
# 나쁜 예

print('hello')
print("world")

a = 'apple'

if True:
    print(True);
else:
    	print(False)
        
b= 'banana'
```



## 2. 들여쓰기

- 문장 구분 시, 들여쓰기를 사용
- 4칸 스페이스 혹은 1탭 → 원칙적으로는 스페이스를 권장



## 3. 변수 (Variable)

- 변수: 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

- 동일 변수에 다른 객체를 언제든 할당할 수 있음.

  즉, 참조하는 객체가 바뀔 수 있기 때문에 '변수'라고 불림.

- 할당 연산자 `=`을 통해 값을 할당(Assignment) → 오른쪽에서 왼쪽으로 읽기

- **`type()`**: 변수에 할당된 값의 타입

- **`id()`**: 변수에 할당된 값의 고유 메모리 주소

- 같은 값을 동시에 할당할 수 O

  ```python
  x = y = 100
  ```

- 다른 값을 동시에 할당할 수 O

  ```python
  x, y = 10, 20
  
  # 각각 값을 바꿔서 저장하기
  # 1. 임시 변수 temp 활용
  # 2. Pythonic
  x, y = y, x
  ```



## 4. 기타

- 사용자 입력: `input()`

  - input()은 str 형태로 저장된다.

  ```python
  name = input('이름을 입력해주세요: ')
  print(name)
  ```

- 주석

  ```python
  # 한 줄 주석
  '''
  여러 줄 주석 1
  '''
  """
  여러 줄 주석 2
  """
  ```

  

# 3. 자료형 (Data Type)

## 1. 자료형 분류

- **Boolean**: 불린형
- Numeric: 수치형
  - int: 정수
  - float: 부동소수점, 실수
  - complex: 복소수
- String: 문자열
- **None**: 값이 없음을 표현. 반환 값이 없는 함수에서 사용.



## 2. Boolean

- True, False(0)의 값

- **`bool()`**: 특정 데이터가 True인지, False인지 검증

- 논리 연산자

  - 논리식을 판단하여, True 혹은 False를 반환
  - and / or / not

  ```python
  num = 100
  num >= 100 and num % 3 == 1	# True
  ```



## 3. Numeric

- 모든 정수의 타입은 `int`

  - long 같은 거 X
  - 매우 큰 수를 나타낼 때 오버플로우 발생하지 X

- 정수가 아닌 모든 실수는 `float`

  - 지수 표기법 사용

  - -1e-100 = 0.00000000000…1

  - 1e-1 = 0.1

  - 실수 연산 과정에서 **Floating point rounding error** 발생 가능

    ```python
    # 아래는 참? 거짓?
    3.14 - 3.02 == 0.12	# False
    
    3.14 - 3.02	# 0.1200000000001
    ```

    ***

    ❣️실수를 비교할 때

    ```python
    # 임의의 작은 수
    abs(a - b) <= 1e-10
    
    # math 모듈 활용
    import math
    math.isclose(a, b)
    ```

- 복소수는 `complex`

- **산술 연산자** (Arithmetic Operator)

  | 연산자 |   내용   |
  | :----: | :------: |
  |   +    |   덧셈   |
  |   -    |   뺄셈   |
  |   *    |   곱셈   |
  | **%**  |  나머지  |
  | **/**  |  나눗셈  |
  | **//** |    몫    |
  | ****** | 거듭제곱 |

- 복합 연산자 (In-place Operator)

  - 연산과 할당이 동시에 이루어짐
  - a += b, a -= b 등

- 비교 연산자 (Comparison Operator)

  | 연산자 |            내용             |
  | :----: | :-------------------------: |
  |   <    |            미만             |
  |   <=   |            이하             |
  |   >    |            초과             |
  |   >=   |            이상             |
  |   ==   |            같음             |
  |   !=   |          같지 않음          |
  |   is   |    객체 아이덴티티(OOP)     |
  | is not | 객체 아이덴티티가 아닌 경우 |



## 4. String

- 모든 문자는 `str`타입

- 작은 따옴표, 큰 따옴표

- 따옴표 안에 따옴표를 표현할 경우

  ```python
  print("문자열 안에 '작은 따옴표'를 표현하려면 큰 따옴표로 묶기")
  print('문자열 안에 "큰 따옴표"를 표현하려면 작은 따옴표로 묶기')
  ```

- 삼중 따옴표

  - 따옴표 안에 따옴표를 넣을 때

  - 여러 줄을 입력할 때

    ```python
    threeQuotes = """
    Python Versions "Compatibility"
    Your source code.
    """
    
    print(threeQuotes)
    ```

    ***

    Python Versions "Compatibility"
    Your source code.

- **`len()`**: str의 길이

- **Indexing**: 인덱스를 통해 특정 값에 접근할 수 있음.

- **Slice**

  ```python
  fruit = 'abcde'
  #  a  b  c  d  e
  #  0  1  2  3  4
  # -5 -4 -3 -2 -1
  
  # Length
  print(len(fruit))	# 5
  
  # Indexing
  print(fruit[1])		# b
  
  # Slicing
  print(fruit[1:3])	# 인덱스 1이상, 3미만 → bc
  print(fruit[-1])	# 마지막 값 (길이 -1 이라고 생각)
  print(fruit[1:4:2])	# b, d
  print(fruit[4:2:-1])	# e, d
  print(fruit[:3])	# a, b, c
  print(fruit[2:])	# c, d, e
  print(fruit[::])	# 그대로 → a, b, c, d, e
  print(fruit[::-1])	# 뒤집기 → e, d, c, b, a
  ```

- `+`: 결합

- `*`: 반복

- **`in`**: 포함

  ```python
  print('a' in 'apple')	# True
  ```

- Escape sequence

  | 예약 문자 |     내용 (의미)      |
  | :-------: | :------------------: |
  |    \n     |    개행 (줄 바꿈)    |
  |    \t     |          탭          |
  |    \r     |     캐리지 리턴      |
  |    \0     |      널 (Null)       |
  |    \\\    |         `\`          |
  |   \\\'    | 단일 인용 부호 (`'`) |
  |   \\\"    | 이중 인용 부호 (`"`) |

- **String Interpolation**: 문자열 안에 변수 넣기

  ```python
  score = 100
  
  # 내 점수는 100이야.
  print('내 점수는 ' + score + '이야.')	# TypeError
  print('내 점수는 ' + str(score) + '이야.')
  print(f'내 점수는 {score}이야.')
  
  # 혹은 % formatting
  ```

- 문자열 특징
  - Immutable: 변경 불가능
  - Iterable: 반복 가능

- 문자열 쪼개기: **`.split(sep)`**

  ```python
  a = '1 2 3'
  
  # 방법 1
  numbers = a.split()
  
  print(numbers)	# ['1', '2', '3']
  
  sum = int(numbers[0]) + int(numbers[1]) + int(numbers[2])	# 6
  
  # 방법 2
  print(sum(map(int, a.split())))	# 6
  ```



## 5. 형 변환 (Typecasting)

- 암시적

  - 사용자 의도 X, 파이썬 내부적으로 변환
  - Bool, Numeric 간의 덧셈

- 명시적: 사용자 의도

  - int, float, str

  - str의 경우, 형식에 맞는 문자열만 변환

    ```python
    int("3.5")		# X
    float("3.5")	# O
    ```



# 4. 컨테이너

## 1. 컨테이너 분류

- 여러 개의 값을 담을 수 있는 객체
- 컨테이너 분류

  - 시퀀스
    - 문자열 (Immutable): 문자들의 나열
    - 리스트 (Mutable): 변경 가능한 값들의 나열
    - 튜플 (Immutable): 변경 불가능한 값들의 나열
    - 레인지 (Immutable): 숫자의 나열
  - 컬렉션
    - 세트 (Mutable): 유일한 값들의 모음 (중복 X)
    - 딕셔너리 (Mutable): 키-값들의 모음



## 2. 시퀀스형

- 시퀀스형 주요 공통 연산자

  | 연산             | 결과                                               |
  | ---------------- | -------------------------------------------------- |
  | s[i]             | s 의 i 번째 항목                                   |
  | s[i:j]           | s 의 i 에서 j - 1 까지의 슬라이스                  |
  | s[i:j:k]         | s 의 i 에서 j - 1 까지 스텝 k 의 슬라이스          |
  | s + t            | s 와 t 이어 붙이기                                 |
  | s * n 또는 n * s | s 를 그 자신에 n 번 더하는 것                      |
  | x in s           | s 의 항목 중 하나가 x 와 같으면 True, 아니면 False |
  | x not in s       | s 의 항목 중 하나가 x 와 같으면 False, 아니면 True |
  | len(s)           | s 의 길이                                          |
  | min(s)           | s 의 가장 작은 항목                                |
  | max(s)           | s 의 가장 큰 항목                                  |



### (1) List

- 변경 가능한 값들의 나열
- 순서가 있고, 다른 타입의 요소를 가질 수 O
- 변경 가능 (Mutable), 반복 가능 (Iterable)
- 대괄호[] 혹은 list()를 통해 생성
- 리스트 값 추가/삭제
  - `.append(element)`: 맨 뒤에 요소 추가
  - `.pop(index)`: 해당 인덱스의 요소 삭제


```python
lst = [90, 100, 60, 70]

print(lst[0])
print(lst[-1])

lst[1] = [50, 50]	# 값 변경 → 리스트 속 리스트
```



### (2) Tuple

- 리스트랑 다 똑같은데, 값 변경만 불가

- 변경 불가능 (Immutable), 반복 가능 (Iterable)
- 소괄호 혹은 tuple()을 통해 생성
- 코딩하면서 굳이 만들 일은 없다.



### (3) Range

- 숫자의 시퀀스를 나타내기 위해 사용
- 파이썬만의 독특한 문법
- 변경 불가능 (Immutable), 반복 가능 (Iterable)
- 기본형: **`range(n)`**
  - 0 부터 n - 1 까지의 숫자 시퀀스
- 범위 지정: **`range(n, m)`**
  - n 부터 m - 1 까지의 숫자의 시퀀스
- 범위 및 스텝 지정: **`range(n, m, s)`**
  - n 부터 m - 1 까지 s 만큼 증가시키는 숫자의 시퀀스



## 3. 컬렉션형 (비시퀀스형)

### (1) Set

- 유일한 값들의 모음

- 순서가 없고, 중복된 값이 없음

  - 수학에서의 집합과 동일한 구조, 집합 연산도 O

- 변경 가능 (Mutable), 반복 가능(Iterable)

- 중괄호 혹은 set()를 통해 생성

  - 단, 빈 중괄호는 딕셔너리

- 값 추가: `.add(element)`

- 값 삭제: `.remove(element)`

- 활용: 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음.

  ```python
  lst = ['서울', '서울', '대전', '광주',
         '서울', '대전', '부산', '부산']
  
  print(set(lst))	# {'서울', '대전', '광주', '부산'}
  print(len(set(lst)))	# 4
  ```



### (2) Dict

- **Key : Value**의 쌍으로 이루어진 모음
- 키 (Key): 불변 자료형만 가능 (리스트, 딕셔너리 불가)
- 값 (Value): 어떠한 형태는 관계 X
- 변경 가능 (Mutable), 반복 가능 (Iterable)

```python
dic = {'1회차' : ['A', 'B'], '2회차' : ['C', 'D']}

print(dic['1회차'])	# ['A', 'B']
```

```python
movie = {
    'title': '설국열차',
    'genres': ['SF', 'Action', 'Drama'],
    'open_date': '2013-08-01',
    'time': 126,
    'adult': False
}

movie['genres']	# ['SF', 'Action', 'Drama']
movie['actors']	# KeyError
```

- 키-값 추가 및 변경

  - 딕셔너리에 키-값의 쌍을 추가할 수 있음.

  - 이미 해당하는 키가 있다면, 기존 값이 변경됨.

    ```python
    dic[key] = value
    ```

- 삭제

  - `.pop(key)`



# 5. 코드업 100제 리뷰

## 1. 6015번

```python
# 1.
numbers = input().split()
a = int(numbers[0])
b = int(numbers[1])
print(a)
print(b)

# 2. 결과를 동시에 할당
a, b = input().split()
print(int(a))
print(int(b))

# 3. map 함수
a, b = map(int, input().split())
print(a)
print(b)
```

