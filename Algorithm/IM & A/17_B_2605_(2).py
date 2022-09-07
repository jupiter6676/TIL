N = int(input())

# 학생들이 뽑은 번호 N개
nums = list(map(int, input().split()))

# 1 ~ N번 학생의 줄 (0 ~ N - 1번)
order = list()

for i in range(N):
    # i번째 학생이 뽑은 수가 0이 아니면
    # 그 수만큼 앞으로 이동
    if nums[i] != 0:
        order.insert(i - nums[i], i)
    else:
        order.append(i)

for i in order:
    print(i + 1, end=' ')