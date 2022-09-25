import sys
sys.stdin = open('input.txt', 'r')

def solution(y, x):
    col = 0
    while True:
        if not (x + col < N):
            break
        
        if graph[y][x + col] == 0:
            break

        col += 1

    row = 0
    while True:
        if not (y + row < N):
            break
        
        if graph[y + row][x] == 0:
            break

        row += 1

    for r in range(y, y + row):
        visited[r][x : x + col] = [1] * col

    return (row * col, row, col)    # 행렬 크기, 행 길이, 열 길이


'''main'''
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    matrixes = list()

    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0 and not visited[i][j]:
                matrixes.append(solution(i, j))

    # 크기가 작은 순서 → 행이 작은 순서로 오름차순 정렬
    matrixes = sorted(matrixes, key=lambda x: (x[0], x[1]))

    # 테스트 케이스, 행렬의 개수 출력
    print(f'#{t} {len(matrixes)}', end=' ')

    # 행렬의 행, 열 길이 출력
    for m in matrixes:
        print(m[1], m[2], end=' ')
    print()