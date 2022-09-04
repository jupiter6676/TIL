# 도화지
graph = [[0] * 101 for _ in range(101)] 

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())

    for i in range(y, y + 10):
        for j in range(x, x + 10):
            graph[i][j] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if graph[i][j]:
            cnt += 1

print(cnt)