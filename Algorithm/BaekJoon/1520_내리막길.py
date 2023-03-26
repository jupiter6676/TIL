import sys
input = sys.stdin.readline

def pprint(mat):
    print('============')
    for row in mat:
        for elem in row:
            print(elem, end='  ')
        print()

def dfs(y, x):
    if y == R - 1 and x == C - 1:
        return 1
    
    # 이미 방문한 곳이면, [y][x]에서 목적지까지 도달할 수 있는 경로의 개수 반환
    if dp[y][x] != -1:
        return dp[y][x]

    # 방문하지 않은 곳이면 계속 탐색
    dp[y][x] = 0

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < R and -1 < nx < C):
            continue

        if graph[ny][nx] < graph[y][x]:
            dp[y][x] += dfs(ny, nx)

    return dp[y][x]
    

'''main'''
R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
dp = [[-1] * C for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

print(dfs(0, 0))
# pprint(dp)