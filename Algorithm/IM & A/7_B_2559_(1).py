N, K = map(int, input().split())
nums = list(map(int, input().split()))

'''
시간 초과
'''
max_ = 0

for i in range(N):
    tmp_sum = 0

    for j in range(i, i + K):
        if j <= N - 1:
            tmp_sum += nums[j]

    max_ = max(max_, tmp_sum)

print(max_)