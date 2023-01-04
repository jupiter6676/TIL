# https://blog.naver.com/occidere/220787441430

N = int(input())

dp = [0] * (N + 1)
dp[1] = 1   # 크기가 1인 2진 수열

if N >= 2:
    dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N])