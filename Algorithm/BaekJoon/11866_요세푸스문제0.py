from collections import deque

N, K = map(int, input().split())
q = deque([i for i in range(1, N + 1)])
seq = list()

cnt = 1
while q:
    pop = q.popleft()

    if cnt == K:
        seq.append(pop)
        cnt = 1
    else:
        q.append(pop)
        cnt += 1

res = '<' + ', '.join(map(str, seq)) + '>'
print(res)