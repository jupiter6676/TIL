import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

dp = [0] * N

dp[0] = nums[0]
if N > 1:
    dp[1] = nums[0] + nums[1]
if N > 2:
    # 1. 한 잔을 건너서 현재 잔을 마심
    # 2. 바로 이전 잔과 현재 잔을 마심
    # 3. 현재 잔을 마시지 X (이전 잔까지 마신 최대 양)
    dp[2] = max(nums[0] + nums[2], nums[1] + nums[2], dp[1])

for i in range(3, N):
    # 1. 한 잔을 건너서 현재 잔을 마심 (dp[i - 2] + nums[i])
    # 2. 바로 이전 잔과 현재 잔을 마심 (dp[i - 3] + nums[i - 1] + nums[i])
    # 3. 현재 잔을 마시지 X (이전 잔까지 마신 최대 양)
    dp[i] = max(dp[i - 3] + nums[i - 1] + nums[i], dp[i - 2] + nums[i])
    dp[i] = max(dp[i], dp[i - 1])

print(max(dp))