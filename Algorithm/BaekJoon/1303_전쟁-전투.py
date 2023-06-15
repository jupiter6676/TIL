import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(y, x):
    global size

    visited[y][x] = 1
    
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if -1 < ny < R and -1 < nx < C:
            if not visited[ny][nx] and graph[ny][nx] == graph[y][x]:
                size += 1
                dfs(ny, nx)


'''main'''
C, R = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
power = [0] * 2 # 백(아군), 청(적군) 위력

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            size = 1    # 뭉쳐있는 아군의 수
            dfs(i, j)

            if graph[i][j] == 'W':
                power[0] += (size ** 2)
            else:
                power[1] += (size ** 2)

print(*power)