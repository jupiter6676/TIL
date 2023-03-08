import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(y, x, height):
    visited[y][x] = 1
    
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < N and -1 < nx < N):
            continue

        if not visited[ny][nx] and graph[ny][nx] > height:
            dfs(ny, nx, height)

    return


'''main'''
N = int(input())
graph = list()
heights = set()
heights.add(0)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(N):
    row = list(map(int, input().split()))

    graph.append(row)
    heights.update(row)

res = 0
for h in heights:
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > h:
                dfs(i, j, h)
                cnt += 1
    
    # print(h, cnt)
    res = max(res, cnt)

print(res)

# visited = [[0] * N for _ in range(N)]
# cnt = 0
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j] and graph[i][j] > 6:
#             dfs(i, j, 6)
#             cnt += 1