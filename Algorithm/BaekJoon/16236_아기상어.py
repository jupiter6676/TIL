import sys
from collections import deque
input = sys.stdin.readline

# 현재 위치에서 물고기 한 마리 먹기?
# 다음 물고기까지의 거리 재기?
def bfs():
    # 상, 좌, 우, 하
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    global size
    cnt = 0
    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < ny < N and -1 < nx < N):
                continue

            # 먹을 수 있는 물고기인 경우
            # 거리를 저장? → 가장 짧은 거리 순으로 정렬하고? 거리 같으면 위쪽으로 이동?
            if graph[ny][nx] and graph[ny][nx] < size:
                visited[ny][nx] = visited[y][x] + 1
                


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
q = deque()

size = 2    # 현재 아기 상어의 크기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            q.append([i, j])
            visited[i][j] = 1

bfs()