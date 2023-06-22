# 1. 코드 리뷰

## (1) 자료구조는 정말 최고야

- https://www.acmicpc.net/problem/23253

- 스택으로 풀려면, top에서 내려오면서 비교를 해야 해.

- 맨 위의 원소를 비교값으로 일단 만들어

- 스택이 빌 때까지 다음을 반복

  - pop한 것과, top에 위치한 값을 비교해
  - 만약 top이 더 크면 pop해서 comparison 갱신
- `input()`보다 `sys.stdin.readline()`이 빠르다

  ```python
  stack = [11, 10, 8, 5]
  comparison = stack.pop()	# 비교할 값
  
  while len(stack) != 0:
      if top > comparison:
      	comparison = stack.pop()
      else:
          answer = 'No'
          break
  ```

- 【코드】

  ```python
  import sys
  input = sys.stdin.readline
  
  N, M = map(int, input().split())
  answer = 'Yes'
  
  for _ in range(N):
      m = int(input())
      stack = list(map(int, input().split()))	# m권의 책 번호
      
      comparison = stack.pop()
  
      while len(stack) != 0:
          # top과 comparison 비교
          if stack[-1] > comparison:
              comparison = stack.pop()	# pop을 사용해 comparison 값 갱신
          else:
              answer = 'No'
              break
  
      # 얘를 써도 OK
      if answer == 'No':
          break
          
  print(answer)
  ```
  



## (2) 괄호

- https://www.acmicpc.net/problem/9012

- 열린 괄호를 넣을 스택과, 닫힌 괄호를 넣을 스택 2개 생성

- 열린 괄호를 만나면 left_stack에 push

  ```python
  bracket = '('
  if bracket == '(':
      left_stack.append(bracket)
  ```

- 닫힌 괄호를 만났을 때, left_stack에 열린 괄호가 있으면 left_stack에서 pop

  ```python
  bracket = '('
  if bracket == ')':
      left_stack.pop()
  ```

- 닫힌 괄호를 만났을 때, 스택의 길이가 0일 때, right_stack에 추가 → **Fail**

  ```python
  bracket = '('
  if bracket == ')':
      if len(left_stack) != 0:
          left_stack.pop()
      else:
          right_stack.append(bracket)
  ```

- 반복문을 다 돌았는데 left_stack에 열린 괄호가 남아있을 때 → **Fail**

  ```python
  LEFT = '('
  RIGHT = ')'
  
  T = int(input())
  for test_case in range(T):
      brackets = list(input())
  
      left_stack = list()
      right_stack = list()
  
      for bracket in brackets:
          # 열린 괄호
          if bracket == LEFT:
              left_stack.append(bracket)
  
          # 닫힌 괄호
          if bracket == RIGHT:
              # 열린 괄호의 스택의 비어있지 않을 때 때
              if len(left_stack) != 0:
                  left_stack.pop()
              # 열린 괄호의 스택이 비어있을 때
              else:
                  right_stack.append(bracket)
  
  if len(left_stack) == 0 and len(right_stack) == 0:
      print('Yes')
  else:
      print('No')
  ```



# 2. 우선순위 큐 (Priority Queue)

- 일반적인 큐는 **순서를 기준**으로, 가장 먼저 들어온 데이터가 가장 먼저 나간다.
- 순서가 아닌 다른 기준으로는?



## (1) 개념

- 순서가 아닌, **우선순위(중요도, 크기 등)를 기준**으로 가져올 요소를 결정(dequeue)하는 큐
- 가장 우선순위가 높은 데이터가 가장 먼저 나가는 방식
- 활용
  - 가중치가 있는 데이터
  - 작업 스케줄링
  - 네트워크
- 대표 동작
  - **enqueue**: 큐의 맨 뒤에 새로운 데이터를 삽입하는 행위
  - **dequeue**: 큐의 맨 앞 데이터(= 가장 우선순위가 높은 데이터)를 빼내어, 가져오는 행위



## (2) 구현

1. 배열 (Array)

2. 연결 리스트 (Linked List)

3. **힙 (Heap)**

4. 구현 별 시간 복잡도

   |      연산 종류      |   Enqueue   |   Dequeue   |
   | :-----------------: | :---------: | :---------: |
   |        배열         |    O(1)     |    O(N)     |
   |    (정렬된 배열)    |    O(N)     |    O(1)     |
   |     연결리스트      |    O(1)     |    O(N)     |
   | (정렬된 연결리스트) |    O(N)     |    O(1)     |
   |       **힙**        | **O(logN)** | **O(logN)** |

   - 가장 작은 원소가 가장 앞에 오도록, 계속 정렬된 상태를 유지
   - 만약 5, 3, 2, 4의 순서로 큐에 원소가 들어오면,
   - 빼낼 때는 2, 3, 4, 5의 순서로 큐에서 나와야 한다.
   - 만약 정렬된 배열로 한다면, Enqueue 시 들어올 때마다 정렬을 해야 하기 때문에 O(N), Dequeue 시 그냥 바로 앞의 것만 빼면 되기 때문에 O(1)



# 3. 힙 (Heap)

## (1) 특징

- **최댓값 또는 최솟값을 빠르게** 찾아내도록 만들어진 자료구조
- 완전 이진 트리의 형태로, **느슨한 정렬 상태를 지속적으로 유지**한다.
  - ex) 첫 번째 인덱스에 가장 작은 값만 오면 돼!
    - 1, 2, 3, 4, 5는 완전한 정렬 상태
    - 1, 3, 2, 5, 4는 느슨한 정렬 상태
- 힙 트리에서는 중복 값을 허용한다.



## (2) 힙은 언제 사용해야 할까?

> Use Cases of Heap

1. 데이터가 지속적으로 정렬되어야 하는 경우
2. 데이터에 삽입/삭제가 빈번할 때
   - Enqueue/Dequeue의 시간 복잡도가 O(logN)
3. 아직까지 원리는 몰라도 된다. 심화에서 트리를 배우고 나서 이해하면 OK!



## (3) 구현

- 파이썬 heapq 모듈

  - Minheap(최소힙)으로 구현되어 있어, 가장 작은 값이 먼저 온다.
  - 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다.
  - 배열, 연결 리스트, 힙으로 직접 구현할 수 있다.

- heapq 연산 종류

  - heapq.heapify(iterable): Destructive method → 원본을 힙으로 변경

  - heapq.heappush(heap)

  - heqpq.heappop(heap, item)

    ```python
    import heapq
    
    nums = [5, 3, 2, 4, 1]
    
    heapq.heapify(nums)	# [1, 3, 2, 4, 5] ← 느슨한 정렬
    
    heapq.heappop(nums)	# [2, 3, 5, 4] ← 2가 앞으로 뿅
    heapq.heappop(nums)	# [3, 4, 5]
    
    heapq.heappush(nums, 10)	# [3, 4, 5, 10]
    heapq.heappush(nums, 0)	# [0, 3, 5, 10, 4]
    ```

- 힙 vs 리스트

  |  연산 종류  |   힙    |     리스트     |
  | :---------: | :-----: | :------------: |
  |  Get Item   |  O(1)   |      O(1)      |
  | Insert Item | O(logN) | O(1) 또는 O(N) |
  | Delete Item | O(logN) | O(1) 또는 O(N) |
  | Search Item |  O(N)   |      O(N)      |



## (4) 예제

- [BOJ 1927번: 최소 힙](https://www.acmicpc.net/problem/1927)

- 【코드】

  ```python
  import heapq
  
  numbers = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]
  heap = list()	# heapify()를 굳이 하지 않아도 OK
  
  for num in numbers:
      if num != 0:
          heapq.heappushheap num)
      else:
          if not len(heap):
              print(0)
          else:
              print(heapq.heappop(heap))
  ```



# 4. 집합 (Set)

## (1) 개념

- 수학에서의 집합을 나타내는 자료구조이다.

- Python에서 기본적으로 제공되는 자료구조이다.

- 연산

  - `.add()`
  - `.remove()`
  - `+` (합), `-` (차), `&` (교), `^` (대칭차)

- 연산의 시간 복잡도

  |  연산 종류  | 시간 복잡도 |
  | :---------: | :---------: |
  |    탐색     |    O(1)     |
  |    제거     |    O(1)     |
  |   합집합    |    O(N)     |
  |   교집합    |    O(N)     |
  |   차집합    |    O(N)     |
  | 대칭 차집합 |    O(N)     |

  



## (2) 집합은 언제 사용해야 할까?

> Use Cases of Set

1. 데이터의 중복이 없어야 할 때 (고유값들로 이루어진 데이터가 필요할 때)
2. **정수가 아닌 데이터**의 삽입/삭제/탐색이 빈번하게 이루어질 때



## (3) 예제

- [BOJ 14425번: 문자열 집합](https://www.acmicpc.net/problem/14425)

- 딕셔너리로 접근해도 OK

- 【코드 1】

  ```python
  S = ['baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh']
  
  words = ['baekjoon', 'codeplus', 'codeminus', 'startlink', 'starlink', 'sundaycoding', 'codingsh', 'codinghs', 'sondaycoding', 'startrink', 'icelink']
  
  cnt = 0
  for word in words:
      if word in S:	# if word in set(S): ← 더 빠르다
          cnt += 1
          
  print(cnt)
  ```

- 【코드 2】

  ```python
  S = ['baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh']
  
  # 얘도 집합으로 간주
  words = ['baekjoon', 'codeplus', 'codeminus', 'startlink', 'starlink', 'sundaycoding', 'codingsh', 'codinghs', 'sondaycoding', 'startrink', 'icelink']
  
  # 교집합의 길이를 출력
  print(len(set(words) & set(S)))
  ```

