import sys
from collections import deque
input = sys.stdin.readline

# 현재 위치에서 물고기 한 마리 먹기
# 다음 물고기까지의 거리 재기
def bfs(y, x):
    min_dist = int(1e9)
    min_y = min_x = int(1e9)

    q.append([y, x])
    visited[y][x] = 1

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < ny < N and -1 < nx < N):
                continue
            
            # 이미 방문한 곳이거나, 자신보다 큰 물고기인 경우
            if visited[ny][nx] or graph[ny][nx] > size:
                continue

            visited[ny][nx] = visited[y][x] + 1

            # 먹을 수 있는 물고기인 경우
            if graph[ny][nx] and graph[ny][nx] < size:
                # 1. 현재 위치의 물고기의 거리가 더 가까운 경우
                # → 거리, 해당 물고기의 좌표 저장
                if min_dist > visited[ny][nx]:
                    min_dist = visited[ny][nx]
                    min_y, min_x = ny, nx

                # 2. 거리가 같은 경우 (= 거리가 가장 가까운 물고기가 여러 마리인 경우)
                # → 현재까지 만난 물고기 중 가장 위쪽, 왼쪽으로 이동
                elif min_dist == visited[ny][nx]:
                    # 현재 위치가 가장 위쪽일 때 → 왼쪽으로 이동하지 않고(min_x = nx), 위쪽으로만 이동하여(min_y = ny) 물고기를 먹음
                    # 여러 물고기가 가장 위쪽에 있을 때 → 왼쪽으로 이동하고(min_x = nx), 위쪽으로는 이동하지 않는다(min_y = ny).
                    if (min_y > ny) or (min_y == ny and min_x > nx):
                        min_y, min_x = ny, nx

            q.append([ny, nx])

    return min_y, min_x


'''main'''
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dy = [-1, 0, 0, 1]  # 상, 좌, 우, 하
dx = [0, -1, 1, 0]
q = deque()

size = 2    # 현재 아기 상어의 크기
y, x = 0, 0 # 현재 아기 상어의 위치
cnt = 0     # 아기 상어가 먹은 물고기의 수
res = 0     # 총 걸리는 시간

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            y, x = i, j
            graph[i][j] = 0 # 아기 상어를 이동시키므로 0으로

while True:
    visited = [[0] * N for _ in range(N)]
    min_y, min_x = bfs(y, x)
    
    # 물고기를 먹었으면 min_y, min_x의 값이 1e9보다 작다.
    if min_y != int(1e9) and min_x != int(1e9):
        res += visited[min_y][min_x] - 1
        cnt += 1
        
        if cnt == size:
            size += 1
            cnt = 0

        graph[min_y][min_x] = 0 # 물고기를 먹으면 빈 칸으로
        y, x = min_y, min_x     # 물고기를 먹은 위치로 상어 이동

    # 물고기를 못 먹는다면, 엄마 상어를 부른다.
    else:
        break

print(res)