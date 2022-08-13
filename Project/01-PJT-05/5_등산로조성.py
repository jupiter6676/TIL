import sys

sys.stdin = open("_등산로조성.txt")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 현재 [y][x] 좌표의 산 높이, 현재까지의 등산로 길이를 인자로
def road(y, x, height, length):
    global flag
    global ans

    # if 0 <= height <= min_h:
    #     lst.append(length)

    visited[y][x] = True

    # 델타 탐색
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < N and -1 < nx < N):
            continue
        
        if not visited[ny][nx]:
            # 산을 한 번 깎았으면 더 이상 깎지 않음.
            if flag:
                if height > graph[ny][nx]:
                    # 높이가 낮은 쪽으로 이동, 등산로 길이 +1
                    road(ny, nx, graph[ny][nx], length + 1)

                    # 백트래킹
                    visited[ny][nx] = False

            # 산을 깎지 않았으면, 모든 경로에 대해 1부터 K까지 깎아봄.
            else:
                for k in range(K + 1):
                    if height > graph[ny][nx] - k:
                        # 단 k = 0인 경우, 산을 깎지 않았으므로 flag = False로 유지
                        flag = True if k != 0 else False
                        
                        # 산이 깎인 만큼의 높이를 넘겨줌.
                        road(ny, nx, graph[ny][nx] - k, length + 1)

                        # 백트래킹 → 산을 깎은 것도 되돌려줌.
                        visited[ny][nx] = False
                        flag = False
    
    # 현재까지의 등산로 중 가장 긴 등산로를 저장
    ans = max(ans, length)

    # 델타 탐색을 더 이상 할 수 없으면, 함수가 종료됨.
    return


T = int(input())

for tc in range(1, T + 1):
    # N * N의 부지, 최대 공사 가능 깊이 K
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]

    flag = False    # 산 깎았는지
    # lst = []
    ans = 0

    max_h = graph[0][0] # 가장 높은 봉우리

    for row in graph:
        max_tmp = max(row)

        if max_h < max_tmp:
            max_h = max_tmp

    # 이차원 리스트 순회
    for i in range(N):
        for j in range(N):
            if graph[i][j] == max_h:
                road(i, j, graph[i][j], 1)

                # 시작 지점을 옮겨야 하므로, 다시 False로 되돌려준다.
                visited[i][j] = False

    # print(f'#{tc}', max(lst))
    print(f'#{tc}', ans)