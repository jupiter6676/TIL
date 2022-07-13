n = int(input())
nums = list(map(int, input().split()))

# 배열 0으로 초기화
cnt = [0 for i in range(24)]

for i in nums:
    cnt[i] += 1

for i in range(1, 24):
    print(cnt[i], end=' ')