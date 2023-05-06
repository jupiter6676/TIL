import sys, copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def bfs():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if -1 < ny < N and -1 < nx < N:
                # 벽이 아닌 경우, 바이러스 퍼뜨리기
                if tmp_graph[ny][nx] != 1 and not visited[ny][nx]:
                    tmp_graph[ny][nx] = 3
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])

def count_time():
    global res
    time = 0

    for i in range(N):
        for j in range(N):
            if tmp_graph[i][j] == 0:
                return False
            
            time = max(time, visited[i][j])

    if time == 0:
        res = 0
    elif time > 0:
        res = min(res, time - 1)

    return True
    

'''main'''
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

coord = list()   # 바이러스를 놓을 수 있는 모든 좌표 순서쌍
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            coord.append([i, j])

viruses_coord = list(combinations(coord, M))  # 모든 좌표 중 M개씩 중복 없는 조합

res = 2501
for viruses in viruses_coord:
    tmp_graph = copy.deepcopy(graph)
    visited = [[0] * N for _ in range(N)]
    q = deque()
    
    # M개의 바이러스 퍼뜨리기
    for virus in viruses:
        y, x = virus
        
        tmp_graph[y][x] = 3 # 바이러스를 3으로 표시
        q.append([y, x])
        visited[y][x] = 1

    bfs()
    count_time()

print(res if res != 2501 else -1)