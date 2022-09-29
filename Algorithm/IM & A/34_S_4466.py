T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    scores.sort(reverse=True)

    sum_ = 0
    for i in range(K):
        sum_ += scores[i]

    print(f'#{t} {sum_}')