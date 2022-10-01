T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    res = 0

    # 가로
    for i in range(N):
        tmp = 0
        for j in range(N):
            if graph[i][j] == 1:
                tmp += 1
            else:
                if tmp == K:
                    res += 1
                tmp = 0

        if tmp == K:
            res += 1

    # 세로
    for j in range(N):
        tmp = 0
        for i in range(N):
            if graph[i][j] == 1:
                tmp += 1
            else:
                if tmp == K:
                    res += 1
                tmp = 0

        if tmp == K:
            res += 1

    print(f'#{t} {res}')