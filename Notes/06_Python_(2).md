# 1. 제어문 (Control Statement)

## 1. 제어문이란

- 파이썬은 기본적으로 위에서 아래로, 순차적으로 명령을 수행
- **순서도로 표현**할 수 있다.



## 2. 제어문의 종류

- 조건문
- 반복문
  - for 문
  - while 문



# 2. 조건문

## 1. 조건문

- 참/거짓을 판단할 수 있는 조건식과 함께 사용

- 형식

  ```python
  if <expression>:
      # Run this code block if expression is True
  else:
      # Run this code block if expression is False
  ```

  - expression에는 참/거짓에 대한 조건식

  - else는 생략 가능

- **【예시】**

  ```bash
  # 홀수인지 확인하는 조건문
  num = int(input())
  if num % 2 == 1:
      print('홀수')
  else:
      print('짝수')
  ```



## 2. 복수 조건문

- 조건식을 동시에 검사하는 것이 아니라, 순차적으로 비교

- 형식

  ```python
  if <expression>:
      # Code block
  elif <expression>:
      # Code block
  elif <expression>:
      # Code block
  else:
      # Code block
  ```

- **【예시】**

  ```python
  dust = int(input())
  
  if dust < 30:
      print("좋음")
  elif dust < 80:
      print("보통")
  elif dust < 150:
      print("나쁨")
  else:
      print("매우나쁨")
  ```



## 3. 중첩 조건문

- 조건문 속 조건문

- 형식

  ```python
  if <expression>:
      # ...
      if <expression>:
          # ...
  else:
      #...
  ```



## 4. 🍁조건 표현식

- 일반적으로 조건에 따라 값을 할당할 때 활용

- 삼항 연산자

- 작성: **<True일 경우의 값> if <expression> else <False일 경우의 값>**

- **【예시】**

  ![조건 표현식](./Assets/06_Python_(2).assets/조건표현식.png)

  ```python
  # 절댓값을 value에 저장
  value = num if num >= 0 else -num
  ```

  ***

  ```python
  num = 2
  result = '홀' if num % 2 else '짝'
  ```



# 3. 반복문

## 1. 반복문의 종류

- while 문
  - **종료조건**에 해당하는 코드로 반복문 종료
- for 문
  - 반복가능한 객체를 모두 순회하면 종료
  - 별도의 종료조건이 필요 X



## 2. while 문

- 조건식이 참인 경우 반복적으로 코드 실행

- 종료조건: 조건식을 False로 만드는 조건

- 형식

  ```python
  while <expression>:
      # Code block
  ```

- **【예시】** 1부터 사용자가 입력한 양의 정수까지의 총합

  ```python
  # 값 초기화
  n = 0
  sum = 0
  user_input = int(input())
  ```

  ```python
  # 1.
  while n <= user_input:
      sum += n
      n += 1
  ```

  ```python
  # 2.
  while n < user_input:
      print(f'n: {n}, sum = {sum}')	# Debugging
      n += 1
      sum += n
  ```



## 3. ☘️for 문

- 시퀀스 (str, tuple, list, range)를 포함한, 순회가능한 객체(Iterable) 요소를 모두 순회함.

- 종료조건이 필요 X

- 형식

  ```python
  for <변수명> in <iterable>:
      # Code block
  ```

- **【예시 1】**

  ```python
  for fruit in ['apple', 'mango', 'banana']:
      print(fruit, end=' ')
  ```

  ***

  apple mango banana



- **【예시 2】 문자열 순회**

  ```python
  string = input()
  
  # 문자열 순회
  for char in string:
      print(char)
  ```

  ```python
  # range를 이용한 문자열 순회
  for i in range(len(string)):
      print(string[i])
  ```



- **【예시 3】 enumerate 순회**

  - 인덱스와 값을 쌍으로 담은 열거형 객체 반환

  - (index, value)의 튜플로 구성

    ```python
    members = ['민수', '영희', '철수']
    
    for i in range(len(members)):
        print(f'{i} {members[i]}')
        
    # enumerate 순회
    for i, member in enumerate(members):
    	print(i, member)
    ```



- **【예시 4】 딕셔너리 순회**

  - **기본적으로 key를 순회**

  - key를 통해 값을 활용

    ```python
    grades = {'john': 80, 'eric': 90}
    
    for name in grades:
        print(name, grades[name])
    ```

    ***

    john 80

    eric 90



## 4. 🍀반복문 제어

1. **`break`**

   - 반복문 종료

   - **【예시 1】**

     ```python
     n = 0
     
     while True:
         if n == 3: break
         print(n, end=' ')
         n += 1
     ```

     ***

     0 1 2

   

   - **【예시 2】**

     ```python
     for i in range(10):
         if i > 1:
             print('0과 1만 필요해!')
             break
         print(i, end=' ')
     ```

     ***

     0 1

     0과 1만 필요해!



2. **`continue`**

   - continue 이후의 코드는 수행하지 않고, 다음 반복을 수행

   - **【예시】**

     ```python
     for i in range(6):
         if i % 2 == 0:
             continue
         print(i, end=' ')
     ```

     ***

     1 3 5



3. 🌿**`for-else`**

   - 끝까지 반복문을 실행한 이후, else 문 실행

   - break를 통해 중간에 종료되는 경우, else 문은 실행되지 X

   - else 문은 break로 중단되었는지 여부에 따라 실행

   - **【예시 1】**

     ```python
     for char in 'apple':
         if char == 'b':
             print('b!')
             break
     
     # break로 중단되지 않으면 실행
     else:
         print('b가 없습니다.')
     ```

     ***

     b가 없습니다.

   

   - **【예시 2】**

     ```python
     for char in 'banana':
         if char == 'b':
             print('b!')
             break
     
     # break로 중단되지 않으면 실행
     else:
         print('b가 없습니다.')
     ```

     ***

     b!



# 4. 기타

- [Python Tutor](https://pythontutor.com/)