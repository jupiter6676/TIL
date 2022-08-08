K = int(input())

for k in range(1, K + 1):
    scores = list(map(int, input().split()))
    
    N = scores[0]
    scores = scores[1:]

    scores.sort(reverse=True)
    
    # 최댓값, 최솟값
    max_ = scores[0]
    min_ = scores[N - 1]

    # 인접 항목들의 차의 최댓값
    largest_gap = 0
    for i in range(N - 1):
        tmp = scores[i] - scores[i + 1]

        if tmp > largest_gap:
            largest_gap = tmp

    print('Class', k)
    print(f'Max {max_}, Min {min_}, Largest gap {largest_gap}')