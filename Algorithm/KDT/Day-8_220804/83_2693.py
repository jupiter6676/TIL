T = int(input())

for _ in range(T):
    nums = set(map(int, input().split()))
    nums = sorted(nums, reverse=True)

    print(nums[2])