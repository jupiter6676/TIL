import sys

sys.stdin = open("_등산로조성.txt")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def road(y, x, height, length):
    global flag

    if 0 <= height <= min_h:
        lst.append(length)

    visited[y][x] = True

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < N and -1 < nx < N):
            continue
        
        if not visited[ny][nx]:
            if flag:
                if height > graph[ny][nx]:
                    road(ny, nx, graph[ny][nx], length + 1)

                    visited[ny][nx] = False
            else:
                for k in range(K + 1):
                    if height > graph[ny][nx] - k:
                        flag = True if k != 0 else False
                        
                        road(ny, nx, graph[ny][nx] - k, length + 1)

                        visited[ny][nx] = False
                        flag = False
    
    return


T = int(input())

for tc in range(1, T + 1):
    # N * N의 부지, 최대 공사 가능 깊이 K
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    stack = list()
    visited = [[False] * N for _ in range(N)]

    flag = False    # 산 깎았는지
    lst = []

    max_h = graph[0][0] # 가장 높은 봉우리
    min_h = graph[0][0] # 가장 낮은 봉우리

    for row in graph:
        max_tmp = max(row)
        min_tmp = min(row)

        if max_h < max_tmp:
            max_h = max_tmp
        if min_h > min_tmp:
            min_h = min_tmp

    # 이차원 리스트 순회
    for i in range(N):
        for j in range(N):
            if graph[i][j] == max_h and not visited[i][j]:
                road(i, j, graph[i][j], 1)
                visited[i][j] = False

    print(f'#{tc}', max(lst))