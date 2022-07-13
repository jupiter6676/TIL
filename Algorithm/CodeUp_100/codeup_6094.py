n = int(input())
nums = list(map(int, input().split()))

# 최솟값
MIN = nums[0]

for i in nums:
    if i < MIN:
        MIN = i

print(MIN)