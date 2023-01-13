# 방법1. -가 나오면 그 뒤의 +는 다 -로 바꾼다.
# 방법2. -를 기준으로 배열을 나눈다.

# 입력: 0-100+50-100+50-100
# -를 기준으로 식 나누기
lst = input().split('-')  # ['0', '100+50', '100+50', '100']

# +가 있는 식 계산해서 새 리스트 만들기
nums = list()
for elem in lst:
    nums.append(sum(map(int, elem.split('+'))))

res = nums[0]   # 첫 번째 수는 빼기 X
for i in range(1, len(nums)):
    res -= nums[i]

print(res)