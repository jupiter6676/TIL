from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
queue = deque()

def bfs():
    queue.append((0, 0))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue

            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                queue.append((ny, nx))

    return maze[N - 1][M - 1]


print(bfs())