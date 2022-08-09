nums = list()

# 5개의 자연수
for _ in range(5):
    nums.append(int(input()))

nums.sort()

print(sum(nums) // 5)   # 평균
print(nums[2])  # 중앙값 (3번째 요소)