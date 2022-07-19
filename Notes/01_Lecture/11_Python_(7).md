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

1. 기본 문법

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



2. 파이썬에서는

   - CamelCase: 클래스

   - snake_case: 변수, 함수



3. 객체 비교하기

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
     - 두 변수의 값을 비교

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

       

4. 인스턴스 메소드

   - 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

     ```python
     class MyClass
     	def instance_method(self, arg1, …)
     ```

   - `self`
     - 인스턴스 자기자신
     - 매개변수 이름을 self로 하여 첫 번째 인자로 정의 (암묵적 규칙)
     - 타 언어의 this 같은 것

   - 생성자(Constructor) 메소드
     - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
     - 인스턴스 변수들의 초기값을 설정
     - `__init__` 
   - 소멸자(Destructor) 메소드
     - 인스턴스 객체가 소멸되기 직전에 호출되는 메소드
     - `__del__`