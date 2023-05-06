import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()
seq = list()

for i in range(1, N + 1):
    q.append(i)

while q:
    for i in range(K - 1):
        pop = q.popleft()
        q.append(pop)

    seq.append(q.popleft())

print('<', end='')
print(*seq, sep=', ', end='')
print('>')

'''
nums = [i for i in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0
i = 0
flag = 0
while True:
    if flag == N:
        break

    if not visited[i]:
        if cnt > 0 and cnt % K == 0:
            seq.append(nums[i])
            visited[i] = 1
            flag += 1

        cnt += 1

    i %= N
    i += 1
'''