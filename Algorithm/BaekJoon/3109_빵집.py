import sys
input = sys.stdin.readline

def dfs(y, x):
    global cnt

    if x == C - 1:
        cnt += 1
        return True # 오른쪽 끝에 도달했으면 True → 모든 재귀 종료

    # 우상, 우, 우하
    dy = [-1, 0, 1]
    dx = [1, 1, 1]

    visited[y][x] = 1

    for d in range(3):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < R and -1 < nx < C):
            continue

        if not visited[ny][nx] and graph[ny][nx] == '.':
            graph[ny][nx] = 'p'

            if dfs(ny, nx):
                return True # 오른쪽 끝에 도달했으면 True → 모든 재귀 종료

    return False    # 모든 델타 탐색 후에도 끝에 도달 못하면 False → 재귀 반복


'''main'''
R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]  # 개행 지우기
visited = [[0] * C for _ in range(R)]

cnt = 0
for i in range(R):
    if not visited[i][0] and graph[i][0] == '.':
        dfs(i, 0)

print(cnt)

# for i in range(R):
#     for j in range(C):
#         print(graph[i][j], end=' ')
#     print()

'''
5 9
.x.....x.
.x..x..x.
.x..x..x.
....x....
.x..x..x.
답: 1
'''