N = int(input())
nums = list(map(int, input().split()))

dp = [nums[0]]

for i in range(1, N):
    # 지금까지 저장한 최댓값(dp[i - 1])에, 현재 수를 더한 것(nums[i])
    # 더했는데 더 작아지면, 연속해서 더하지 않고 처음(nums[i])부터 더하기
    dp.append(max(nums[i] + dp[i - 1], nums[i]))

print(max(dp))