import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited[1][0][0] = 1
    q.append([1, 0, 0])

    while q:
        break_cnt, y, x = q.popleft()

        if y == N - 1 and x == M - 1:
            return visited[break_cnt][y][x]

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < ny < N and -1 < nx < M):
                continue

            if graph[ny][nx] == 1 and break_cnt:
                visited[0][ny][nx] = visited[1][y][x] + 1
                q.append([0, ny, nx])
                
            if graph[ny][nx] == 0 and not visited[break_cnt][ny][nx]:
                visited[break_cnt][ny][nx] = visited[break_cnt][y][x] + 1
                q.append([break_cnt, ny, nx])

    return -1
                

'''main'''
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]   # visited[i][y][x]: i는 부술 수 있는 벽의 수

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
q = deque()

print(bfs())