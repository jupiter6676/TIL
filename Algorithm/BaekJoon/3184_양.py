import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def pprint(mat):
    print('==========')
    for row in mat:
        for elem in row:
            print(elem, end=' ')
        print()

def dfs(y, x):
    global sheep, wolf

    if not visited[y][x]:   # 중복 카운트 피하기
        if graph[y][x] == 'o':
            sheep += 1
        if graph[y][x] == 'v':
            wolf += 1

    visited[y][x] = 1

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if -1 < ny < R and -1 < nx < C:
            if graph[ny][nx] != '#' and not visited[ny][nx]:
                dfs(ny, nx)


R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
total = [0] * 2 # 아침에 살아있는 양, 늑대

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'o' or graph[i][j] == 'v':
            if not visited[i][j]:
                sheep = wolf = 0
                dfs(i, j)

                if sheep > wolf:
                    total[0] += sheep
                else:
                    total[1] += wolf

# pprint(visited)
print(*total)