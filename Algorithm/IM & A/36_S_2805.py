T = int(input())
for t in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    start_j = N // 2
    end_j = N // 2 + 1

    sum_ = 0
    for i in range(N):
        for j in range(start_j, end_j):
            sum_ += graph[i][j]

        if i < N // 2:
            start_j -= 1
            end_j += 1
        else:
            start_j += 1
            end_j -= 1

    print(f'#{t} {sum_}')