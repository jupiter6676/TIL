import sys
input = sys.stdin.readline

def bfs(y, x, d):
    dy = [-1, 0, 1, 0]  # 북동남서
    dx = [0, 1, 0, -1]

    global res

    turn = 0    # 현재 칸에서 둘러본 주변 칸의 수
    while True:
        if graph[y][x] == 0:
            graph[y][x] = 2
            res += 1
        
        for i in range(4):
            # d: 0(N) → nd: 3(W)
            # d: 1(E) → nd: 0(N)
            # d: 2(S) → nd: 1(E)
            # d: 3(W) → nd: 2(S)
            nd = (3 + d - i) % 4    # 바라보던 방향의 반시계 방향부터 시작, 총 4 방향으로 바라본다.
            ny = y + dy[nd]         # 바라보는 방향의 칸의 좌표를 (ny, nx)에 저장한다.
            nx = x + dx[nd]

            if not (-1 < ny < R and -1 < nx < C):
                continue

            # 둘러보다가 청소되지 않은 칸이 있으면, 그 쪽으로 전진한다.
            if graph[ny][nx] == 0:
                graph[ny][nx] = 2
                res += 1

                y = ny
                x = nx
                d = nd

                turn = 0    # 다시 초기화
                break

            else:   # 벽이나 청소된 칸을 보면
                turn += 1
            
            # 주위 4칸 모두 청소되지 않은 칸이거나 벽이면, 현재 보는 방향의 반대로 이동
            if turn == 4:
                nd = (2 + d) % 4
                ny = y + dy[nd]
                nx = x + dx[nd]
                
                if graph[ny][nx] == 1:
                    return
                else:
                    y = ny
                    x = nx
                    # d는 유지

                turn = 0
                
                
def pprint(mat):
    for i in range(R):
        for j in range(C):
            print(mat[i][j], end=' ')
        print()



R, C = map(int, input().split())
start_y, start_x, d = map(int, input().split()) # d: 0 → N, 1 → E, 2 → S, 3 → W
graph = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
res = 0

bfs(start_y, start_x, d)
print(res)
# print('========')
# pprint(graph)