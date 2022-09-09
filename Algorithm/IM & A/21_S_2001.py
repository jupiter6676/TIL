# import sys

# sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    for i in range(N):
        for j in range(N):
            tmp_sum = 0

            for y in range(M):
                for x in range(M):
                    if not (i + y >= N or j + x >= N):
                        tmp_sum += graph[i + y][j + x]

            max_sum = max(max_sum, tmp_sum)

    print(f'#{t} {max_sum}')