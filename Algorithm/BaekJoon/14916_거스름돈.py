import sys
input = sys.stdin.readline

N = int(input())
dp = [50001] * (N + 1)
dp[0] = 0

if N >= 2:
    dp[2] = 1

if N >= 5:
    dp[5] = 1

for i in range(2, N - 1):
    if i + 2 <= N:
        if dp[i + 2]:
            dp[i + 2] = min(dp[i + 2], dp[i] + 1)
        else:
            dp[i + 2] = dp[i] + 1

    if i + 5 <= N:
        if dp[i + 5]:
            dp[i + 5] = min(dp[i + 5], dp[i] + 1)
        else:
            dp[i + 5] = dp[i] + 1

print(dp[N] if dp[N] != 50001 else -1)