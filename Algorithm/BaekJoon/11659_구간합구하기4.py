import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)  # prefix sum

for i in range(1, N + 1):
    dp[i] = dp[i - 1] + nums[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])    # i번째 수도 합에 포함