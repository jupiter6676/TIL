import sys
from collections import deque
input = sys.stdin.readline

def pprint(mat):
    print('==========')
    for row in mat:
        for elem in row:
            print(elem, end=' ')
        print()

def bfs():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque([[0, 0]])   # 가장자리의 외부 공기

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if -1 < ny < R and -1 < nx < C:
                if graph[y][x] == 0 and visited[ny][nx] != -1:
                    if graph[ny][nx]:
                        visited[ny][nx] += 1
                    
                    else:
                        visited[ny][nx] = -1
                        q.append([ny, nx])

                        
def melt():
    for i in range(R):
        for j in range(C):
            if visited[i][j] >= 2:
                graph[i][j] = 0

def is_finish():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 1:
                return False
            
    return True


R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

res = 0
while True:
    visited = [[0] * C for _ in range(R)]
    
    if is_finish():
        print(res)
        break

    bfs()
    melt()
    # pprint(visited)
    # pprint(graph)
    res += 1