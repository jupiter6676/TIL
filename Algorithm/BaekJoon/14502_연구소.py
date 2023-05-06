import sys, copy
from collections import deque
from itertools import product, combinations

input = sys.stdin.readline

def pprint(mat):
    print('===================')
    for i in range(N):
        for j in range(M):
            print(mat[i][j], end=' ')
        print()

def bfs():
    visited = [[0] * M for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    q = deque()
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                q.append([i, j])

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if -1 < ny < N and -1 < nx < M:
                # 벽이 아닌 경우, 바이러스 퍼뜨리기
                if tmp_graph[ny][nx] == 0 and not visited[ny][nx]:
                    tmp_graph[ny][nx] = 2
                    visited[ny][nx] = 1
                    q.append([ny, nx])

def count_safe():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 0:
                cnt += 1

    return cnt


'''main'''
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

coord = list(product(range(N), range(M)))   # 모든 좌표 순서쌍
walls_coord = list(combinations(coord, 3))  # 모든 좌표 중 3개씩 중복 없는 조합
# print(walls_coord)

res = 0
for walls in walls_coord:
    tmp_graph = copy.deepcopy(graph)
    
    # 3개의 벽 세우기
    for wall in walls:
        y, x = wall

        if tmp_graph[y][x]:
            break   # 벽이 3개가 되지 않는 경우, break

        tmp_graph[y][x] = 1

    # 벽이 3개 세워진 경우, bfs
    else:
        bfs()
        res = max(res, count_safe())
        
print(res)