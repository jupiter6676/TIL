N = int(input())
dp = [0] * (N + 1)

dp[0] = 1

if N > 1:
    dp[2] = 3

    # 3 × i, i는 짝수
    for i in range(4, N + 1, 2):
        dp[i] = dp[i - 2] * dp[2]

        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2

print(dp[N])