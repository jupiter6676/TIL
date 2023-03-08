def dfs(y, x):
    global house_cnt

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    visited[y][x] = 1

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < N and -1 < nx < N):
            continue
        
        if not visited[ny][nx] and graph[ny][nx]:
            house_cnt += 1
            dfs(ny, nx)



N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

res = list()

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]:
            house_cnt = 1   # 단지 내 집 수
            dfs(i, j)
            res.append(house_cnt)

res.sort()

print(len(res))
for num in res:
    print(num)