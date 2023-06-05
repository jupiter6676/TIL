import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if -1 < ny < R and -1 < nx < C:
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    graph[ny][nx] = 1
                    visited[ny][nx] = visited[y][x] + 1

                    q.append([ny, nx])

def check():
    global res
    time = 0

    for i in range(R):
        for j in range(C):
            if graph[i][j] == 0:
                return False
            
            time = max(time, visited[i][j])

    res = time
    return True


'''main'''
C, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
q = deque()

for i in range(R):
    for j in range(C):
        if graph[i][j] == 1:
            q.append([i, j])

bfs()

res = 0
if not check():
    res = -1

print(res)