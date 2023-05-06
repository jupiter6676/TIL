import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    cnt = 1

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if -1 < ny < N and -1 < nx < M:
                if not graph[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
                    cnt += 1

    return cnt
    

'''main'''
N, M, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
res_list = list()

q = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(N):
    for j in range(M):
        if not graph[i][j] and not visited[i][j]:
            visited[i][j] = 1
            q.append([i, j])
            res_list.append(bfs())

res_list.sort()
print(len(res_list))
print(*res_list)