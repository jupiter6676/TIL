# 1. 객체 지향 프로그래밍 (OOP)

- 파이썬은 모든 것이 객체
- **객체**
  - 클래스에서 정의한 것을 토대로 메모리에 할당된 것
  - 변수, 자료구조, 함수, 메소드, 클래스, 인스턴스 등 '**모든 것**'
  - 객체는 **클래스**(타입, 종류)의 **인스턴스**(값, 실제 사례)
    - 123, 900, 5는 모두 int의 인스턴스
    - 'hello', 'bye'는 모두 str의 인스턴스
  - 특징
    - **타입**(type): 어떤 연산자와 조작이 가능한가?
    - **속성**(attribute): 어떤 상태(데이터)를 가지는가?
    - **조작법**(method): 어떤 행위(함수)를 할 수 있는가



- 객체 지향 프로그래밍?

  - 컴퓨터 프로그래밍의 패러다임 중 하나

    - 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나,
    - 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법
    - vs 절차 지향 프로그래밍
      - 메서드 없이, 함수 내에서 함수를 부르고…

  - 특징

    - 추상화: 현실 세계를 프로그램 설계에 반영

    - 클래스, 인스턴스, 속성, 메소드

      ```python
      # 클래스 선언
      class Person:
          # 속성: name, age, gender
          # 생성자 메소드
          def __init__(self, name, age, gender):
              self.name = name
              self.age = age
              self.gender = gender
              
          # info() 메소드: 클래스 내부 정의 함수
          def info(self):
              return (self.name, self.age, self.gender)
      ```

      ```python
      # 인스턴스: hong, ko
      hong = Person('홍길동', 100, 'M')
      ko = Person('고길동', 40, 'M')
      
      print(hong.info())	# ('홍길동', 100, 'M')
      print(hong.name)	# 홍길동
      print(type(hong))	# <class '__main__.Person'>
      ```



# 2. OOP 기초

## (1) 기본 문법

```python
# 클래스 정의
class MyClass:
    pass

my_instance = MyClass()	# 인스턴스 생성
my_instance.my_method()	# 메소드 호출
my_instance.my_method()	# 속성
```

- 클래스와 인스턴스
  - 클래스: 객체들의 분류
  - 인스턴스: 하나하나의 실체, 예
  - 파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스

- 속성
  - 특정 데이터 타입/클래스의 객체들이 가지게 될 상태, 데이터

- 메소드
  - 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위, 함수



## (2) 파이썬에서 이름 짓기

- CamelCase: 클래스

- snake_case: 변수, 함수



## (3) 객체 비교하기

- 얕은 복사 vs 깊은 복사

  ```python
  a = [1, 2, 3]
  b = a	# 얕은 복사
  
  # 깊은 복사
  c = list(a)	# 리스트 형변환
  d = a[::]	# 슬라이싱
  
  # but
  a = [[1, 2], 3, 4]
  b = list(a)
  
  b[0][0] = 'hi'
  print(a)	#[['hi', 2], 3, 4]
  print(b)	#[['hi', 2], 3, 4]
  # 1차원 상의 리스트는 나뉘어 다른 주소를 가리키지만, 
  # a[0][0]와 b[0][0]은 같은 주소를 가리킴.
  
  # 진짜 깊은 복사 하려면
  import copy
  e = copy.deepcopy(a)
  ```

  

- `==`
  - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
  
- **`is`**

  - 두 변수가 동일한 객체를 가리키는 경우 True

  - 값이 아닌 메모리 주소를 비교

    ```python
    a = [1, 2, 3]
    
    b = [1, 2, 3]
    print(a == b, a is b)	# True False
    
    b = a	# 얕은 복사 (b도 a와 같은 객체를 가리킴)
    print(a == b, a is b)	# True True
    ```

    

## (4) 인스턴스

- 인스턴스 변수
  - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
  - 각 인스턴스들의 고유한 변수
- 생성자 메소드에서 self.<name>으로 정의
- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당



## (5) 인스턴스 메소드

- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드

- 클래스 내부에 정의되는 메소드의 기본

- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

  ```python
  class MyClass
  	def instance_method(self, arg1, …)
  ```

- `self`
  - 인스턴스 자기자신
  - 인스턴스 메소드를 호출 시, 첫 번째 인자로 인스턴스 자신이 전달되게 설계
    - 매개 변수 이름으로 self를 첫번째 인자로 정의
  - 개별 인스턴스 각각에 속성을 지정하거나, 가져올 수 있음.
  - 타 언어의 this 같은 것
  
- 생성자(Constructor) 메소드
  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
  - 인스턴스 변수들의 초기값을 설정
  - `__init__` 메소드 자동 호출
  
- 소멸자(Destructor) 메소드
  - 인스턴스 객체가 소멸되기 직전에 호출되는 메소드
  - `__del__`



# 3. 클래스

## (1) 클래스 속성

- 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성

- 클래스 선언 내부에서 정의

- <classname>.<name>으로 접근 및 할당

  ```python
  class Circle:
      pi = 3.14
  ```

  ```python
  c1 = Circle()
  c2 = Circle()
  ```

  ```python
  print(Circle.pi)	# 3.14
  print(c1.pi)	# 3.14
  print(c2.pi)	# 3.14
  ```

  

- 인스턴스와 클래스 간의 이름 공간

  - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
  - 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
  - 인스턴스에서 특정 속성에 접근하면, 인스턴스 → 클래스 순으로 탐색



## (2) 클래스 메소드

- 클래스가 사용할 메소드

- @classmethod 데코레이터를 사용하여 정의

  - 데코레이터: 함수를 어떤 함수로 꾸며서 새로운 기능을 부여

- 호출 시, 첫 번째 인자로 클래스(cls)가 전달됨.

  - cls는 암묵적으로 붙이는 이름

  ```python
  class MyClass:
  	@classmethod
      def class_method(cls, arg1, …)
  ```



## (3) 스태틱 메소드

- 내부에서 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드

- 속성을 다루지 않고 단지 기능(행동)만을 하는 메소드️를 정의할 때 사용

- @staticmethod 데코레이터를 사용하여 정의

  - 호출 시, 어떠한 인자도 전달되지 X (클래스 정보에 접근, 수정 불가)
  
  ```python
  class MyClass:
  	@staticmethod 
      def static_method()
  ```
  



## (4) 메소드 정리

- 인스턴스 메소드
  - 호출한 인스턴스를 의미하는 self 매개변수를 통해 인스턴스를 조작
- 클래스 메소드
  - 클래스를 의미하는 cls 매개변수를 통해 클래스를 조작
- 스태틱 메소드
  - 인스턴스나 클래스를 의미하는 매개변수는 사용하지 X
    - 즉, 객체 상태나 클래스 상태는 수정할 수 X
  - 일반 함수처럼 동작하지만 클래스의 이름 공간에 귀속됨.
    - 주로 해당 클래스로 한정하는 용도로 사용



## (5) 클래스 예시

```python
class MyClass:
    class_var = '클래스 변수'
    
    # 메소드 정의
    def __init__(self):
        self.instance_var = '인스턴스 변수'
    
    # 인스턴스 메소드 정의
    def instance_method(self):
        return self, self.instance_var
    
    # 클래스 메소드 정의
    @classmethod
    def class_method(cls, arg1, …):
        return cls, cls.class_var
    
    # 스태틱 메소드 정의
    @staticmethod
    def static_method():
        return '스태틱'
```

```python
c1 = MyClass()
print('인스턴스 변수 호출', c1.instance_var)
print('인스턴스 메소드 호출', c1.instance_method())
print('클래스 메소드 호출', c1.class_method())
print('스태틱 메소드 호출', c1.static_method())
```



# 4. 객체지향의 핵심 개념️

## (1) 추상화

- 몰라도 되는 정보는 가리고, 꼭 알아야 되는 정보만 나타내는 것



## (2) 상속

1. 상속

   - 두 클래스 사이 부모-자식 관계를 정립하는 것

   - 클래스는 상속이 가능, 모든 파이썬 클래스는 object를 상속받음.

   - 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음.

   - 코드 재사용성 증가



2. 상속 관련 함수와 메소드

   - `isinstance(object, classinfo)`
     - classinfo의 instance거나, subclass*인 경우 True

   - `issubclass(class, classinfo)`
     - class가 classinfo의 subclass면 True
     - classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사

   - **`super()`**
     
     - super는 상위 클래스를 의미
     - 자식 클래스에서 부모 클래스를 사용하고 싶은 경우
     
     ```python
     class Person:
         def __init__(self, name):
             self.name = name
     ```
     
     ```python
     class Student(Person):
         def __init__(self, name, age):
             super().__init__(name)	# Person 클래스
             self.age = age
     ```



3. 상속 정리
   - 파이썬의 모든 클래스는 object로부터 상속됨.
   - 부모 클래스의 모든 요소(속성, 메소드)가 상속됨.
   - `super()`를 통해 부모 클래스의 요소를 호출할 수 있음.
   - 메소드 오버라이딩을 통해 자식 클래스에서 재정의 가능함.
   - 상속관계에서의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색함.
   - 다중 상속이 가능함.



## (3) 다형성

- 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음.
- 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답될 수 있음.
- **메소드 오버라이딩**
  - 상속받은 메소드를 재정의
  - 클래스 상속 시, 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경
  - 부모 클래스의 메소드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용



## (4) 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
- 파이썬에서 기능상으로 존재하지 않지만, 관용적으로 사용되는 표현이 있음
  - Public: 어디서나
  - Protect: 부모, 자식
  - Private: 본인(클래스)