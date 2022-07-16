# 1. 스택과 큐

## (1) 스택

- 먼저 들어온 데이터가 나중에 나가는 **선입후출**의 자료구조

- **입구와 출구가 동일**한 형태로 시각화    ex) 박스 쌓기

- 연산: 삽입, 삭제



## (2) 스택 구현 예제

1. Python
   
   - **리스트**로 구현!
   
   - 리스트의 **`append()`, `pop()` 메서드**의 시간복잡도는 **상수 시간 O(1)**
   
   - 따라서 스택 자료구조는 리스트로 구현하기에 적합하다.
   
   ```python
   stack = list()
   
   # 삽입(5), 삽입(2), 삽입(3), 삽입(7), 삭제(), 삽입 (1), 삽입(4), 삭제()
   stack.append(5)
   stack.append(2)
   stack.append(3)
   stack.append(7)
   stack.pop()
   stack.append(1)
   stack.append(4)
   stack.pop()
   
   print(stack[::-1)    # 최상단 원소부터 출력 → [1, 3, 2, 5]
   ```



2. C++

   - stl 라이브러리에서 스택 자료구조를 지원


   - `push()`, `pop()`, `top()` 함수 활용

   ```cpp
   #include <bits/stdc++.h>
   
   using namespace std;
   
   stack<int> s
   
   int main(void)
   {
       s.push(5);
       s.push(2);
       s.push(3);
       s.push(7);
       s.pop();
       s.push(1);
       s.push(4);
       s.pop();
   
       // 스택 최상단 원소부터 출력 → 1 3 2 5
       while (!s.empty())
       {
           cout << s.top() << ' ';
           s.pop();
       }
   }
   ```



3. Java

   - `push()`, `pop()`, `peek()` 메서드 활용

   ```java
   import java.util.*;
   
   public class Main
   {
       public static void main(String[] args)
       {
           Stack<Integer> s = new Stack<>();
   
           s.push(5);    
           s.push(2);
           s.push(3);
           s.push(7);
           s.pop();
           s.push(1);
           s.push(4);
           s.pop();
   
           // 스택 최상단 원소부터 출력 → 1 3 2 5
           while (!s.empty())
           {
               System.out.print(s.peek() + " ");
               s.pop();
           }
       }
   }
   ```



## (3) 큐

- 먼저 들어온 데이터가 먼저 나가는 **선입선출**의 자료구조

- **입구와 출구가 모두 뚫려있는, 터널**과 같은 형태로 시각화

- ex) 은행 창구



## (4) 큐 구현 예제

1. Python

   - **deque 라이브러리** 사용❣️

   - 리스트를 이용해 구현할 수 있지만, 시간복잡도가 높아 비효율적

   - `append()`
     
     - 리스트의 append와 동일한 기능 → 가장 오른쪽에 원소를 추가
     
     - 시간복잡도 O(1)

   - `popleft()`
     
     - 가장 왼쪽의 원소를 제거
     
     - 시간복잡도 O(1)

   ```python
   from collections import deque
   
   queue = deque()
   
   queue.append(5)
   queue.append(2)
   queue.append(3)
   queue.append(7)
   queue.popleft()
   queue.append(1)
   queue.append(4)
   queue.popleft()
   
   print(queue)    # 먼저 들어온 순서대로 출력 → deque([3, 7, 1, 4)]
   queue.reverse()
   print(queue)    # 나중에 들어온 원소부터 출력 → deque([4, 1, 7, 3)]
   ```



2. C++

   - `push()`, `pop()`, `front()` 함수 사용

   ```cpp
   #include <bits/stdc++.h>
   
   using namespace std;
   
   queue<int> q
   
   int main(void)
   {
       q.push(5);
       q.push(2);
       q.push(3);
       q.push(7);
       q.pop();
       q.push(1);
       q.push(4);
       q.pop();
   
       // 먼저 들어온 원소부터 출력 → 3 7 1 4
       while (!q.empty())
       {
           cout << q.front() << ' ';
           q.pop();
       }
   }
   ```



3. Java

   - `offer()`, `poll()` 함수 사용

   ```java
   import java.util.*;
   
   public class Main
   {
       public static void main(String[] args)
       {
           // 큐 중에서도 연결 리스트 형식
           Queue<Integer> q = new LinkedList<>();
   
           q.offer(5);    
           q.offer(2);
           q.offer(3);
           q.offer(7);
           q.poll();
           q.offer(1);
           q.offer(4);
           q.poll();
   
           // 먼저 원소부터 추출 → 3 7 1 4
           while (!q.empty())
           {
               System.out.print(s.poll() + " ");
           }
       }
   }
   ```

   
