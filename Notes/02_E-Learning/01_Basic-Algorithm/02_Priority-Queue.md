# 2. 우선순위 큐 (Priority Queue)

- 우선순위가 가장 높은 데이터를 가장 먼저 삭제

- ex) 물건 데이터를 자료구조에 넣었다가, 가치가 높은 물건부터 꺼내서 확인해야 하는 경우
  
  | 자료구조   | 추출되는 데이터        |
  | ------ | --------------- |
  | 스택     | 가장 나중에 삽입된 데이터  |
  | 큐      | 가장 먼저 삽입된 데이터   |
  | 우선순위 큐 | 가장 우선순위가 높은 데이터 |



## (1) 우선순위 큐 구현

1. 구현 방법

   - 리스트를 이용

   - 힙 (Heap)을 이용

   - 데이터가 N개일 때의 시간 복잡도 비교
     
     | 구현 방식 | 삽입 시간   | 삭제 시간   |
     | ----- | ------- | ------- |
     | 리스트   | O(1)    | O(N)    |
     | 힙     | O(logN) | O(logN) |



2. **힙 정렬**

   - 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일하다. (힙에 넣었다 빼면 정렬된다.)


   - 시간 복잡도는 **O(NlogN)**



## (2) 힙 (Heap)

1. 힙의 특징

   - 완전 이진 트리 자료구조의 일종


   - 항상 **루트 노드** (Root Node)를 제거


   - **최소 힙** (Min Heap)
     - 루트 노트가 가장 작은 값
     
     - 값이 작은 데이터가 우선적으로 제거
     

   - **최대 힙** (Max Heap)
     - 루트 노드가 가장 큰 값
     
     - 값이 큰 데이터가 우선적으로 제거



2. 완전 이진 트리 (Complete Binary Tree)
   - 루트 노드부터 시작해, 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리



3. 최소 힙 구성 함수

   - Min-Heapify()

   - 상향식

     - 부모 노드로 거슬러 올라가며,

     - 부모보다 자신의 값이 더 작은 경우 위치를 교체

       ![image-20220716152841526](02_PriorityQueue.assets/image-20220716152841526.png)

   

   - 힙에 새로운 원소가 삽입될 때

     - O(logN)의 시간 복잡도로 힙 성질을 유지할 수 있다.

       ![2022-07-16-153934](02_PriorityQueue.assets/2022-07-16-153934.png)

   

   - 힙에서 원소가 제거될 때

     - O(logN)의 시간 복잡도로 힙 성질을 유지할 수 있다.

     - 원소를 제거할 때, 가장 마지막 노드가 루트 노드의 위치에 오도록 한다.

       ![2022-07-16-154241](02_PriorityQueue.assets/2022-07-16-154241.png)

     - 이후에 루트 노드에서부터 하향식으로(더 작은 자식 노드로) Heapify()를 진행한다.

       ![2022-07-16-154442](02_PriorityQueue.assets/2022-07-16-154442.png)



## (3) 힙 정렬 구현 예제

> 우선순위 큐 라이브러리 활용



1. Python

   - heapq 라이브러리
   - 파이썬의 heapq 라이브러리는 **기본적으로 Min Heap** (오름차순 정렬)
   - **Max Heap**을 구현하고 싶다면, 원소를 넣을 때와 꺼낼 때 -1을 붙이면 된다.

   ```python
   import sys
   import heapq
   
   input = sys.stdin.readline
   
   def heapsort(iterable):	# list, tuple...
       h = list()
       result = list()
       
       # 모든 원소를 차례대로 힙에 삽입
       for value in iterable:
           heapq.heappush(h, value)
           
       # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
       for i in range(len(h)):
           result.append(heapq.heappop(h))
           
       return result
   
   
   n = int(input())
   arr = list()
   
   for i in range(n):
       arr.append(int(input()))
       
   res = heapsort(arr)
   
   for i in res:
       print(i)
   ```



2. C++

   - C++의 우선순위 큐 라이브러리는 **기본적으로 Max Heap**

   ```cpp
   #include <bits/stdc++.h>
   
   using namespace std;
   
   int n;
   vector<int> arr;
   
   // 하나의 벡터 객체가 있을 때, 그 reference를 참조
   void heapSort(vector<int>& arr)
   {
       priority_queue<int> h;
       
       // 모든 원소를 차례대로 힙에 삽입
       for (int i = 0; i < arr.size(); i++)
           h.push(-arr[i]);
           
       // 힙에 삽입된 모든 원소를 차례로 꺼내어 출력
       while (!h.empty())
       {
           printf("%d\n", -h.top());
           h.pop();
       }
   }
   
   int main()
   {
       cin >> n;
       
       for (int i = 0; i < n; i++)
       {
           int x;
           scanf("%d", &x);
           arr.push_back(x);
       }
       
       heapSort(arr);
   }
   ```
