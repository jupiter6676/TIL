# 1. 코드 리뷰 (220729)

## (1) 암호문

- https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14w-rKAHACFAYD

- 파이썬은 `.insert()` 메소드를 통해 쉽게 풀 수 있다.

- 각각의 명령어의 위치를 파악한다

  ![image-20220801092044042](Assets/19_Data-Structure_(4)_Stack_Queue.assets/image-20220801092044042.png)

  - I x y s → **x: 0 + 1, y: 0 + 2, s: [0 + 3 : 0 + 3 + y]**❣️

  - ```python
    명령어 = 명령어리스트[0]
    if 명령어 == 'I':
        x = 명령어리스트[0 + 1]
        y = 명령어리스트[0 + 2]
        숫자리스트 = 명령어리스트[0 + 3 : 0 + 3 + y]
    ```

- 그런데 슬라이싱을 하면 리스트로 반환되는데, insert의 값에는 숫자 혹은 문자열만 들어갈 수 있다.

- **숫자 리스트를 역순**으로 돌면, 같은 인덱스만 가리키며 삽입하면 순서대로 삽입된다.❣️

  ```python
  명령어 = 명령어리스트[0]
  if 명령어 == 'I':
      x = 명령어리스트[0 + 1]
      y = 명령어리스트[0 + 2]
      숫자리스트 = 명령어리스트[(0 + 3) : (0 + 3 + y)]
  
      for 숫자 in 숫자리스트[::-1]:
          암호문.insert(삽입인덱스, 숫자)
  
      0 -> 1
  ```

- 【코드】

  ```python
  T = 10
  
  for test_case in range(1, T + 1):
      origin_len = int(input())	# 원본 암호문의 길이
      origin_code = list(map(int, input().split()))	# 원본 암호문
      
      command_len = int(input())	# 명령어의 개수
      command_list = input().split()
      
      i = 0
      while i < len(command_list):
          command = command_list[i]
          if command == 'I':
              # x, y, 숫자리스트 s 구하기
              x = int(command_list[i + 1])
              y = int(command_list[i + 2])
              num_list = command_list[i + 3 : i + 3 + y]
              
              # x의 위치에 숫자들을 삽입한다.
              # 역순으로 삽입한다.
              for num in num_list[::-1]:
                  origint_code.insert(x, int(num))
                  
  		i += 1
     
  	# * 붙이면 리스트가 unpacking 되어서 출력된다.
  	print(f'#{test_case}', *origint_code[:10])
  ```



# 2. 스택 (Stack)

- Stack은 쌓는다는 의미로, 마치 접시를 쌓고 빼듯이 **데이터를 한 쪽에서만 넣고 빼는 자료구조**
- 가장 마지막에 들어온 데이터가 가장 먼저 나가므로, **LIFO**(Last-In First-Out, 후입선출) 방식
- 대표 동작
  - **push**: 스택에 새로운 데이터를 삽입하는 행위
  - **pop**: 스택의 가장 마지막 데이터(= 가장 최신의 데이터)를 빼내어, 가져오는 행위



## (1) 왜 스택을 써야할까?✨

> Use Cases of Stack

1. **뒤집기, 되돌리기, 되돌아가기**

   - 스택은 들어온 순서와 나가는 순서가 반대이다.
   - ex) 브라우저 뒤로 가기, ctrl + z, 단어 뒤집기

2. **마무리 되지 않은 일을 임시 저장**

   - ex) 괄호 매칭: 괄호 열고 닫기가 제대로 되었는지 검사

   - ex) 함수 호출(재귀 호출): 함수 인자로 함수 넣기

     - ```python
       print(sum(max(min(2, 5), 10), min(2, 5)))
       ```

     - sum → max() → min(2, 5)  → max(2, 10) → min(2, 5) → sum(10, 2) → print(12)

   - ex) 백트래킹: 미로 찾기, n-queens

   - ex) DFS



## (2) 구현

- 스택은 **리스트**로 간편하게 구현할 수 있다.

  - push → `.append()`
  - pop → `.pop()`
  - 각 메소드의 시간 복잡도는 O(1)

- 다른 언어들은 연결 리스트로 직접 구현해야 한다.

  ![image-20220801105048228](Assets/19_Data-Structure_(4)_Stack_Queue.assets/image-20220801105048228.png)

## (3) 예제

> 문제 이해: 쓸데 없는 내용 제거(이름 등) → 요점 파악 → 핵심 내용 파악 → 예제 입출력 확인

- [BOJ 10773번: 제로](https://www.acmicpc.net/problem/10773)

- 접근 방법

  - if 0이 아니면, 계속 입력 (스택에 push)
  - else 0이면, 가장 최신값 삭제 (스택에서 pop)

- 【코드 1】

  ```python
  input1 = [3, 0, 4, 0]
  input2 = [1, 3, 5, 4, 0, 0, 7, 0, 0, 6]
  
  stack = list()
  for elem in input1:
      if num != 0:
  		stack.append(elem)
      else:
          stack.pop()
          
  print(sum(stack))
  ```

- 【코드 2】 Input Handling

  ```python
  N = int(input())
  input_list = list()
  
  for _ in range(N):
      input_list.append(int(input()))
      
  stack = list()
  for elem in input_list:
      if num != 0:
  		stack.append(elem)
      else:
          stack.pop()
          
  print(sum(stack))
  ```

- 【코드 3】 입력과 동시에, 스택 연산 수행

  ```python
  N = int(input())
  
  stack = list()
  for _ in range(N):
      num = int(input())
      
      if num != 0:
  		stack.append(elem)
      else:
          stack.pop()
          
  print(sum(stack))
  ```



# 3. 큐 (Queue)

- 큐는 **한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조**
- 가장 먼저 들어온 데이터가 가장 먼저 나가므로, **FIFO**(First-in First-out, 선입선출) 방식
- 대표 동작
  - **enqueue**: 큐의 맨 뒤에 새로운 데이터를 삽입하는 행위
  - **dequeue**: 큐의 맨 앞 데이터(= 가장 오래된 데이터)를 빼내어, 가져오는 행위



## (1) 구현

- 큐도 **리스트**로 간편하게 구현할 수 있다.

  - enqueue→ `.append()`
  - dequeue→ `.pop()`
  - 단점: dequeue 시 시간복잡도가 O(N)이 된다. 뺀 후 앞으로 데이터를 당겨줘야 하기 때문.

- **덱**(**Deque**, Double-Ended Queue) 자료구조

  ![image-20220801114339247](Assets/19_Data-Structure_(4)_Stack_Queue.assets/image-20220801114339247.png)

  - **양 방향으로 삽입과 삭제가 자유로운 큐**

  - 양 방향 삽입, 추출이 모두 큐보다 훨씬 빠르다.

  - 넣을 때 `append()`, 뺄 때 `popleft()`

  - ```python
    from collections import deque
    
    nums = [1, 2, 3, 4, 5]
    
    queue = deque(nums)	# deque 객체 생성, 인자로 seq, iterable 인자
    queue.append(6)
    queue.popleft()
    
    print(queue)	# deque([2, 3, 4, 5, 6])
    print(list(queue))	# [2, 3, 4, 5, 6]
    print(queue, end=' ')	# 이러면 하나씩 출력된대 or 반복문
    ```



## (2) 예제

- [BOJ 2161번: 카드1](https://www.acmicpc.net/problem/2161)

- 접근 방법

  - 제일 위에 있는 카드를 버리기 → popleft()
  - 버린 후 제일 위에 있는 카드를 버린 후 카드 밑으로 옮기기 → q.append(q.popleft())
  - 카드가 1개 남았을 때 종료
  - 출력
    - 카드를 뺄 때마다 출력
    - 리스트에 pop한 것들을 다 모아서 출력

- 【코드】

  ```python
  from collections import deque
  
  n = int(input())
  queue = deque()
  ```

  
