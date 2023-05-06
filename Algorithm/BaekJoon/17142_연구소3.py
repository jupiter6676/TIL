import sys, copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def pprint(mat):
    print('===================')
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=' ')
        print()

def bfs():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    global res
    time = 0    # 바이러스가 퍼지는 데 걸리는 시간 (!= 비활성 바이러스로 이동하는 시간)
    infected_area = 0   # 바이러스가 퍼진 넓이 (비활성 바이러스는 이미 퍼져있다고 간주)

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if -1 < ny < N and -1 < nx < N:
                if tmp_graph[ny][nx] != 1 and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])

                    if tmp_graph[ny][nx] == 0:
                        infected_area += 1
                        time = visited[ny][nx]

    # 모든 빈 공간을 전염시켰다면
    if infected_area == empty_area:
        if time > 0:
            time -= 1

        res = min(res, time)


'''main'''
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

coord = list()  # 비활성 바이러스
empty_area = 0  # 빈 공간의 넓이
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            coord.append([i, j])

        elif graph[i][j] == 0:
            empty_area += 1

viruses_coord = list(combinations(coord, M))  # 비활성 바이러스 좌표 중 M개씩 중복 없는 조합

res = 2501
for viruses in viruses_coord:
    tmp_graph = copy.deepcopy(graph)
    visited = [[0] * N for _ in range(N)]
    q = deque()

    for virus in viruses:
        y, x = virus

        q.append([y, x])
        visited[y][x] = 1

    bfs()
    # pprint(visited)

print(res if res != 2501 else -1)

'''
4 2
0 1 1 0
2 1 1 2
2 1 1 2
0 1 1 0
답: 2

5 3
2 2 2 0 0
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
답: 2

5 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
2 0 0 2 0
1 1 1 1 1
답: 2

5 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
0 2 0 2 0
1 1 1 1 1
답: 3
'''