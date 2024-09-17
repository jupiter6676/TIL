import sys
input = sys.stdin.readline

'''
3 4 6
....
.T..
....
'''

def pprint(array_2d):
    print("=============================")
    for row in array_2d:
        for elem in row:
            print(elem, end=" ")
        print()

def dfs(y, x, length):  # 현재 (y, x) 좌표, 이동 거리
    # pprint(visited)
    global result

    visited[y][x] = length

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if not(-1 < ny < R and -1 < nx < C):
            continue

        if graph[ny][nx] == 'T' or visited[ny][nx]:
            continue

        if length <= K:
            dfs(ny, nx, length + 1)
            visited[ny][nx] = 0

    if length == K:
        if y == 0 and x == C - 1:
            result += 1
        else:
            return

'''main'''
R, C, K = map(int, input().split()) # 행, 열, 이동 가능 횟수
graph = [list(input().strip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
result = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

dfs(R - 1, 0, 1)    # 이동 거리는 시작 지점 포함 (1부터 시작)
print(result)
