N = int(input())
nums = list(map(int, input().split()))  # 1, 2, 3, ..., N
dp = [0] * (N + 1)  # 0, 1, 2, 3, ..., N

max_asc = 0
for i in range(N):
    n = nums[i]

    dp[n] = dp[n - 1] + 1   # d = 1인 가장 긴 등차수열 찾기
    max_asc = max(max_asc, dp[n])

print(N - max_asc)