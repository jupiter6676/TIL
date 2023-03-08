'''
N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]   # [i][j]: j로 "시작하는" i자리 수
dp[1][:] = [1] * 10

for i in range(2, N + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][j :])

print(sum(dp[N]) % 10007)
'''

N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]   # [i][j]: j로 "끝나는" i자리 수
dp[1][:] = [1] * 10

for i in range(2, N + 1):
    for j in range(10):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        dp[i][j] %= 10007

print(sum(dp[N]) % 10007)