import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * (1000001)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for t in range(T):
    N = int(input())

    for i in range(4, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

    print(dp[N])

'''
import sys
input = sys.stdin.readline

dp = [1,2,4,7]
for i in range(int(input())):
    n = int(input())
    for j in range(len(dp), n):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[n-1])
'''