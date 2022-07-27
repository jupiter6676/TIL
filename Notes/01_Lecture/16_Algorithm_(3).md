# 1. 코드 리뷰 (220726)

## (1) 오르막길

![image-20220727092013346](Assets/16_Algorithm_(3).assets/image-20220727092013346.png)

- 뒤에 있는 값을 기준으로, 이전의 값과 비교
  - heights[i - 1] < heights[i]
- 그런데 idx = 0부터 시작한다면?
  - heights[0] > heights[-1]
  - **idx = 1부터** 시작
- 오르막 첫 값과 끝 값만 구해서 빼는 건 어려움
  - 오르막 끝에 갈 때까지 **누적합**을 구하자



1. 답을 담는 변수 없이, 바로 print

   ```python
   N = int(input())
   
   # 높이 리스트 입력
   heights = list(map(int, input().split()))
   
   sum_ = 0	# 누적합 저장 변수
   sum_list = list()	# 누적합들을 저장할 변수
   
   # 오르막길을 찾기 위해서 인덱싱
   for i in range(1, len(heights)):
       # 오르막길: 현재 값 > 이전 값
       if heights[i] > heights[i - 1]:
           sum_ += heights[i] - heights[i - 1]
           
           # 오르막길일 때마다 누적합을 저장
           # 어짜피 max해서 나오는 것이 답이기 때문에 이렇게 저장해도 OK
           # 여기에 하거나 (1)
           sum_list.append(sum_)
           
   	# 오르막길이 아니면
       else:
           sum_list.append(sum_)
           sum_ = 0
   
   # 여기에 하거나 (2)
   # sum_list.append(sum_)
   
   # 만약 오르막길이 없으면 0을 출력
   if len(sum_list) == 0:
       print(0)
   else:
       print(max(sum_list))
   ```



2. 답을 담는 변수 max_sum

   ```python
   sum_ = 0	# 누적합 저장 변수
   max_sum = 0	# 최대 합을 저장할 변수
   
   # 오르막길을 찾기 위해서 인덱싱
   for i in range(1, len(heights)):
       if heights[i] > heights[i - 1]:
           sum_ += heights[i] - heights[i - 1]
           
           # 기존의 가장 긴 높이와, 현재 높이를 비교해서
           # 긴 높이를 저장
           max_sum = max(max_sum, sum_)
       else:
           sum_ = 0
   ```



3. 특정 오르막길의 끝 값과 시작 값을 빼서 오르막길의 길이 구하기❣️

   ```python
   '''
   5
   5 2 1 4 6
   '''
   import sys
   sys.stdin = open('오르막길.txt')
   
   N = int(input())	# N: 리스트 길이
   
   # 높이 리스트 입력
   heights = list(map(int, input().split()))
   
   # 가장 긴 오르막길 길이를 저장할 변수
   max_h = 0
   
   # 오르막길 시작, 끝 값 변수
   start = 0
   end = 0
   
   for i in range(1, len(heights)):
       # 오르막길이 진행중
       if heights[i] > heights[i - 1]:
           # 오르막길이 시작 전일 때만 시작 값 start를 변경
           # 이 조건이 없으면, 오르막길이 발생할 때마다 시작 값이 변경된다.
           if start == 0:
               start = heights[i - 1]
               
           if i == len(heights) - 1:
               end = heights[i]
               max_h = max(max_h, end - start)
               
           # 오르막길이 아닌데 start != 0이라면
           # 오르막길을 다 지나와 오르막이 끝났다는 뜻
           else:
               # start가 0이라면, 오르막길을 시작하지 않았다는 의미
               # 따라서, start가 0이 아닐 때 오르막길의 끝 값을 구하고,
               # 오르막길의 길이를 계산한다.
               if start != 0:
                   end = heights[i - 1]
                   
                   # 끝 값과 첫 값을 사용해 오르막길 길이를 구한다.
                   length = end - start
                   
                   # 가장 긴 길이를 갱신한다.
                   max_h = max(max_h, length)
                   
                   # 오르막길의 시작 값을 0으로 초기화한다.
                   start = 0
                   
   print(max_h)
   ```



## (2) 분해합

- N이 주어지면, N의 생성자 M을 구하기 위해 1부터 N - 1까지 모든 경우의 수를 탐색한다.
- M을 분해해서, M과 M의 각 자리수를 더한 값이 N이 되면 M은 N의 생성자이다.
- 더 빠르게 하고 싶다면, (자릿수 × 10) 범위만 찾으면 된다.
  - 여기서는 X

```python
N = int(input())

# 1부터 N - 1까지 모든 수의 분해합을 탐색
for num in range(1, N):
    split_num = 0	# 분해합 저장 변수
    
    # 각 자릿수의 합
    for digit in str(num):
        split_sum += int(digit)
        
    # 각 자릿수의 합 + 수의 합 → 분해합
    split_sum += num
    
    # 구한 분해합과 입력 N이 같으면, 그 num은 N의 생성자
    if N == split_sum:
        print(num)
        break	# 가장 작은 생성자를 탐색하기 때문에, 찾으면 바로 종료
        
# for-else
# break를 만나지 않으면 (= 생성자가 없으면 0을 출력)
else:
	print(0)
```



# 2. 문자열

- 문자열은 immutable 자료형
- 문자열 슬라이싱이나 Concatenate 등을 할 때, 원래의 것이 바뀐 게 아니라, 새로 만들어진 무언가가 나온다.



## (1) 문자열 조작

- ```python
  word = 'apple'
  word += 'banana'
  ```

  이렇게 하면, word는 'apple'을 가리키다가 'banana'를 가리키게 된다.

  그러면 apple은 자동으로 사라지게 된다.



- ```python
  s = 'abcdefghi'
  s[2:5]	# 'cde'
  ```

  슬라이싱도 문자열 원본이 바뀌는 게 아니라, 문자열을 조작한 결과를 반환하는 것.

  \+ 추가 팁: (문자열의 길이 - 해당 문자의 인덱스)를 한 뒤 부호를 뒤집으면 마이너스 인덱스가 된다!



## (2) 문자열 관련 메소드

1. `.split()`
   - 문자열을 일정 기준으로 나누어 리스트로 반환
   - 괄호 안에 아무것도 넣지 않으면, 자동으로 공백을 기준으로 설정
2. `.strip()`
   - 문자열 양쪽 끝에 있는 특정 문자를 모두 제거한 새로운 문자열 반환
   - 괄호 안에 아무것도 넣지 않으면, 자동으로 공백을 제거
   - 제거할 문자를 여러 개 넣으면, 해당하는 모든 문자들을 제거
3. `.find(문자)`
   - 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환
   - 찾는 문자가 없다면 -1 반환
4. `.index(문자)`
   - 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환
   - 찾는 문자가 없다면 오류 발생 → 그 즉시 실행 중단
5. `.count(문자)`
   - 문자열에서 특정 문자가 몇 개인지 반환
   - 문자 뿐만 아니라, 문자열의 개수도 확인 가능
6. `.replace(기존 문자, 새로운 문자)`
   - 문자열에서 기존 문자를 새로운 문자로 수정한 새로운 문자열 반환
   - 특정 문자를 빈 문자열("")로 수정하여, 마치 해당 문제를 삭제한 것 같은 효과도 가능
   - 시간 복잡도 O()
7. `삽입할 문자.join(iterable)`
   - iterable의 각각 원소 사이에 특정 문자를 삽입한 새로운 문자열 반환
   - 공백 출력, 콤마 출력 등 원하는 출력 형태를 위해 사용



# 3. 아스키(ASCII) 코드

- 컴퓨터는 숫자만 이해할 수 있다!
  - 비트: 0과 1 두 가지 정보만 표현
  - 바이트: 데이터를 저장하는 기본 단위 (1byte = 8bits)
- 그렇다면 문자는 어떻게 저장될까? → ASCII
  - 알파벳을 표현하는 대표 인코딩 방식
  - 각 문자를 표현하는 데 1byte 사용
    - 1bit는 통신 에러 검출용 (글자인지 아닌지)
    - 7bit는 문자 정보 저장 (총 128개)
- `ord(문자)`
  - 해당 문자의 아스키 코드 값을 반환
- `chr(아스키 코드)`
  - 아스키 코드에 해당하는 문자를 반환



# 4. 기타

- https://github.com/kdt-hphk/01-resources/tree/master/python/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%2003

- [http://channy.creation.net/blog/1663](https://www.youtube.com/redirect?event=live_chat&redir_token=QUFFLUhqblZYbXNXci1YSXB1bHgxaEZQbkxTNnVzODVQZ3xBQ3Jtc0tsSlNaOVZZRW50UHphY200VXFYTjljNzVKQ2E3RU1uREJqT1Rmci1ETVpfc3VKM3RkN0xJMklFVnJBZjNMMmptMDVORWlmUF9iaE00a3RiejE2VnlHc0p1N3RFUHJ2ZWNSSHlTMWtmbElvQ21YZmdVQQ&q=http%3A%2F%2Fchanny.creation.net%2Fblog%2F1663)