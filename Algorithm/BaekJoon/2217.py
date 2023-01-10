N = int(input())
nums = list()

for _ in range(N):
    nums.append(int(input()))

nums.sort(reverse=True) # 내림차순 정렬

# nums의 최솟값 * 로프 개수가 최대 중량
# 로프를 N개 선택, N - 1개 선택 … 1개 선택하는 모든 경우
max_res = 0
for _ in range(N):
    max_res = max(max_res, nums[-1] * len(nums))
    nums.pop()

print(max_res)

'''
3
10
5
15

3개 다 쓰면 15밖에 못 함
2개만 써도 되니까 20이 최대
'''