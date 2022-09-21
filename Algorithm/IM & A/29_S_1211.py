import sys
sys.stdin = open('input.txt', 'r')

def ladder(y, x):
    visited = [[0] * 100 for _ in range(100)]

    # 좌, 우, 하
    dx = [-1, 1, 0]
    dy = [0, 0, 1]

    visited[y][x] = 1

    while True:
        if y == 99:
            break

        for d in range(3):
            ny = y + dy[d]
            nx = x + dx[d]

            if not (0 <= ny < 100 and 0 <= nx <100):
                continue

            if graph[ny][nx] == 0:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                y = ny
                x = nx

    return visited[y][x]

for _ in range(1, 11):
    t = int(input())

    graph = [list(map(int, input().split())) for _ in range(100)]
    dists = list()

    for j in range(100):
        if graph[0][j] == 1:
            dists.append([j, ladder(0, j)]) # 출발점과 거리의 쌍을 저장

    # 거리를 기준으로 오름차순 정렬
    dists = sorted(dists, key=lambda x: x[1])

    print(f'#{t} {dists[0][0]}')

'''
1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1

18 15 18 25
'''