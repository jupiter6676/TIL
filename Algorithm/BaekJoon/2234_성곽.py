import sys
from collections import deque
input = sys.stdin.readline

def pprint(mat):
    print('=============')
    for row in mat:
        for elem in row:
            print('%3d' % elem, end=' ')
        print()

def bfs(py, px, room_cnt):
    visited[py][px] = room_cnt
    q.append([py, px])
    room_size = 1    # 방 넓이

    while q:
        y, x = q.popleft()

        for d in range(4):
            # & 연산 시 1, 2, 4, 8이 나오면 그 방향에 벽이 있다는 뜻
            if (graph[y][x] & walls[d] == walls[d]):
                continue

            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < ny < R and -1 < nx < C):
                continue
            
            if not visited[ny][nx]:
                visited[ny][nx] = room_cnt
                q.append([ny, nx])
                room_size += 1

    return room_size    

'''main'''
C, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

q = deque()
dy = [1, 0, -1, 0]      # SENW
dx = [0, 1, 0, -1]      # SENW
walls = [8, 4, 2, 1]    # SENW

rooms = list()  # 각 방의 넓이

room_cnt = 0
max_room_size = 0
for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            room_cnt += 1
            max_room_size = max(max_room_size, bfs(i, j, room_cnt))

print(room_cnt)
print(max_room_size)

for i in range(R):
    for j in range(C):
        # 시작 좌표의 벽을 없앤 후 bfs 진행 (모든 좌표에 대해)
        for d in range(4):  # (한 좌표의 모든 벽을 없앨 수 있도록)
            if (graph[i][j] & walls[d] == walls[d]):    # 벽이 있다면
                visited = [[0] * C for _ in range(R)]
                graph[i][j] -= walls[d] # 벽을 없앰
                max_room_size = max(max_room_size, bfs(i, j, 1))    # 그 벽을 없애고 bfs 진행
                graph[i][j] += walls[d] # 벽을 다시 세우고, 다른 벽을 없앤다.

                # pprint(visited)

print(max_room_size)