from collections import deque

N = int(input())
q = deque()

for num in range(1, N + 1):
    q.append(num)

# 큐의 원소가 하나가 남을 때까지 반복
while len(q) > 1:
    # 맨 앞 원소 제거
    pop = q.popleft()
    print(pop, end=' ')

    # 제거된 원소 바로 다음 원소 제거
    pop = q.popleft()
    q.append(pop)   # 제거 후 맨 뒤에 append

# 큐에 남은 마지막 원소 제거 후 출력
print(q.popleft())