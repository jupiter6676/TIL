# 0. 함수 (Function)

```python
len('happy!')
```

```python
word = 'happy!'
cnt = 0
for char in word:
	cnt += 1
```

- 위 2개는 모두 같은 기능을 한다.

- 우리는 왜 함수를 사용할까?

  → Decomposition, Abstraction

- **Decomposition**

  - 기능을 분해하여 재사용 가능

- 💕**Abstraction** (추상화)

  - 복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음. (블랙박스)

  - 재사용성, 가독성, 생산성

  - 예를 들어,

    print()라는 함수가 어떻게 구현되어 있는지 알 필요 X. 다만 print()를 쓰는 방법만 안다면 우리도 쓸 수 있음.

    이처럼, input을 넣으면, 어떻게 함수가 동작하는지는 몰라도 output이 나온다는 것이 핵심!



# 1. 함수의 정의

- 함수
  - 특정 기능을 하는 코드의 조각
  - 필요 시 간단하게 호출하여 사용
- 함수 사용 이유
  - 코드 중복 방지
  - 재사용 용이



# 2. 함수의 종류

1. 사용자 함수 (Custom Function)

   ```python
   def function_name(parameter):
       # Fuction body
       return return_value
   ```

   ***

   ```python
   # 함수 선언
   def foo():
       return True
   
   def add(x, y):
       return x + y
   
   # 함수 호출
   foo()
   add(2, 3)
   ```

2. 내장 함수 (Built-in Function)

3. 외장 함수 (라이브러리)



# 3. 함수의 결과값 (Output)

- **`return`**

  - 함수는 반드시 값을 하나만 return

  - 명시적 return이 없으면 None을 반환

    - ex. print() 함수는 출력만 해주고, 반환값은 None

  - return과 동시에 함수 종료

  - 두 개 이상의 값을 반환하고 싶으면

    ```python
    def minus_and_product(x, y):
        return x - y, x * y	# tuple의 형태로 반환
    ```



# 4. 함수의 입력 (Input)

```python
def add(x, y):	# Parameter
    return x + y

add(2, 3)	# Argument
```

- Parameter: 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- Argument: 함수를 호출할 때, 넣어주는 값

  - 함수 호출 시 함수의 parameter를 통해 전달되는 값
  - 필수 Argument: 반드시 전달되어야 하는 Argument
  - 선택 Argument
    - 값을 전달하지 않아도 되는 경우
    - 기본 값이 전달



## 1. Argument의 종류

1. **Positional Argument** (기본)

   ```python
   def add(x, y):
       return x + y
   
   add(2, 3)	# 2와 3이 각각 x, y에 대응됨.
   ```

   - 함수 호출 시 Argument는 위치에 따라 함수에 전달된다.



2. **Keyword Argument**

   ```python
   def add(x, y):
       return x + y
   
   add(x=2, y=5)
   add(2, y=5)
   ```

   - 변수의 이름을 통해 직접 특정 Argument를 전달할 수 O

   - Keyword Argument 다음에 Positional Argument를 활용할 수 X



3. **Default Arguments Values**

   ```python
   def add(x, y=0):
       return x + y
   
   add(2)
   ```

   - 기본값을 지정해, 호출 시 Argument 값을 설정하지 않도록 함.
   - print()의 sep의 기본값은 ' '으로 정의되어 있음.



4. **정해지지 않은 개수의 Arguments**

   ```python
   def my_func(*args):
       return args
   
   res = my_func(1, 2, 3)
   print(type(res))	# <class 'tuple'> → 값 변경 X
   ```



5. **정해지지 않은 개수의 Keyword Arguments**

   ```python
   def my_func(**kargs):
       return kargs
   
   res = my_func(name='홍길동', age='20', gender='M')
   print(type(res))	# <class 'dict'>
   ```



# 5. 함수의 범위 (Scope)

- 함수는 코드 내부에 Local scope를 생성, 그 외의 공간 Global scope로 구분

- 객체 수명주기❣️

  - Built-in Scope: 파이썬이 실행된 이후부터 영원히 유지
  - Global Scope: 모듈이 호출된 시점 이후, 혹은 인터프리터가 끝날 때까지 유지
  - Local Scope: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

- 이름 검색 규칙 (Name Resolution) ❣️

  - 파이썬에서 사용되는 이름 (식별자)들은 이름공간 (namespace)에 저장되어 있다.

  - LEGB Rule: 아래와 같은 순서로 이름을 찾아나감.

    - Local Scope: 함수
    - Enclosed Scope: 특정 함수의 상위 함수 (함수 속 함수)
    - Global Scope: 함수 밖 변수, Import 모듈
    - Built-in Scope: 파이썬 안에 내장되어 있는 함수 또는 속성

  - 함수 내에서는 바깥 Scope의 변수에 접근 가능하지만, 수정할 수는 X

    ```python
    sum = 5
    print(sum([1, 2, 3]))
    
    # TypeError: 'int' object is not callable
    # Built-in Scope에 sum 함수가 있었음.
    # Global Scope에 sum 이름의 변수를 만들었음.
    # L → E → G → B의 순으로 찾음.
    # 즉, sum이 지금은 5가 되어버림.
    ```



# 6. 함수 응용

- **`map()`**

  - 반복(순회) 가능한 것들의 모든 요소에, 어떤 함수를 모두 적용시킨 결과로 map object를 반환

  - map(function, iterable)

    ```python
    numbers = ['1', '2', '3']
    new_numbers = map(int, numbers)	# 숫자로 바꾸기
    
    print(new_numbers, type(new_numbers))	# <map object at 0X…> <class 'map'>
    print(list(nuew_numbers))	# list로 형변환해서 보면 바뀌어 있다.
    ```

    ---

    ![map](./Assets/07_Python_(3).assets/map.png)

    ```python
    # 두 개의 정수가 공백을 사이에 두고 입력될 때
    n, m = map(int, input().split())
    
    # input()의 타입은 항상 str
    # split()으로 문자열 쪼갬
    # split()의 반환 결과는 항상 list
    # int 함수를 input().split() 리스트의 모든 요소에 적용한 결과
    ```



# 7. 기타

- [파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html)

- [파이썬 자습서](https://docs.python.org/ko/3/tutorial/index.html)
