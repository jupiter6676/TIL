n = int(input())    # 필요없는 거 같은데
nums = list(map(int, input().split()))

for i in nums[::-1]:
    print(i, end=' ')

'''
for i in range(n-1, -1, -1):
  print(nums[i], end=' ')
'''