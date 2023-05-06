import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global res
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    time = 0    # 시간 경과
    while q_h:
        time += 1

        # 물 채우기
        while q_water and q_water[0][2] < time:
            y, x, t = q_water.popleft()

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if -1 < ny < R and -1 < nx < C:
                    if graph[ny][nx] == '.':
                        graph[ny][nx] = '*'
                        q_water.append([ny, nx, t + 1])

        # 고슴도치 이동
        while q_h and q_h[0][2] < time:
            y, x, t = q_h.popleft()


            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if ny == end_y and nx == end_x:
                    res = t + 1
                    return True
                
                if -1 < ny < R and -1 < nx < C:
                    if graph[ny][nx] == '.' and not visited[ny][nx]:
                        visited[ny][nx] = 1
                        q_h.append([ny, nx, t + 1])
        
    return False


'''main'''
R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

q_h = deque()
q_water = deque()
end_y = 0
end_x = 0
res = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            q_h.append([i, j, 0])
        if graph[i][j] == '*':
            q_water.append([i, j, 0])
        if graph[i][j] == 'D':
            end_y = i
            end_x = j

print(res if bfs() else 'KAKTUS')