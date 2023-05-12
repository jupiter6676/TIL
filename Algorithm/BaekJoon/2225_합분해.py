import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 1000000000

# dp[k][n] = k개의 수로 n을 만드는 경우의 수
dp = [[0] * (N + 1) for _ in range(K + 1)]

dp[0][0] = 1

for k in range(1, K + 1):
    for n in range(N + 1):
        for i in range(n + 1):
            # k - 1개의 수로 n - i를 만드는 경우의 수를 더한다.
            dp[k][n] += dp[k - 1][n - i]
            dp[k][n] %= MOD

# print(dp)
print(dp[K][N])