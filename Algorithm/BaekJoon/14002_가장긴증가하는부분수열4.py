N = int(input())
seq = list(map(int, input().split()))

dp = [[] for _ in range(N)]

for i in range(N):
    if not dp[i]:
        dp[i].append(seq[i])

    for j in range(i):  # 0 ~ i - 1 수들을 탐색
        # j번째 수가 i번째 수보다 작으면 (→ 증가하는 부분 수열)
        if seq[j] < seq[i]:
            # 1. i번째 수까지의 증가하는 부분 수열의 길이
            # 2. (j번째 수까지의 증가하는 부분 수열 + i번째 수) 수열의 길이
            if len(dp[i]) < len(dp[j] + [seq[i]]):
                dp[i] = dp[j] + [seq[i]]    # 2번이 더 크면 2번의 수열을 저장

# print(dp)
dp.sort(key=lambda x: -len(x))
print(len(dp[0]))
print(*dp[0])

'''
4
1 4 2 3
답: 3 / 1 2 3

6
97 90 75 78 67 30
답: 2 / 75 78

12
349 459 138 262 99 693 106 762 122 553 96 514
답: 4 / 349 459 693 762

10
1 2 4 5 3 6 7 8 9 10
답: 9 / 1 2 4 5 6 7 8 9 10
'''