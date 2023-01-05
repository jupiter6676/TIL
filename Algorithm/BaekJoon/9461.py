T = int(input())
for t in range(T):
    N = int(input())
    dp = [1, 1, 1, 2, 2]

    for i in range(5, N):
        dp.append(dp[i - 1] + dp[i - 5])    # dp[i - 2] + dp[i - 3]

    print(dp[N - 1])