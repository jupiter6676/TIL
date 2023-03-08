N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort()

for num in nums:
    print(num)