N = int(input())

# 학생들이 뽑은 번호 N개
nums = list(map(int, input().split()))

# 1 ~ N번 학생의 줄 (0 ~ N - 1번)
order = [i for i in range(N)]

for i in range(N):
    tmp_order = list()

    # i번째 학생이 뽑은 수가 0이 아니면
    # 그 수만큼 앞으로 이동
    if nums[i] != 0:
        for j in range(i - nums[i]):
            tmp_order.append(order[j])

        tmp_order.append(i)

        for j in range(i - nums[i], N):
            if order[j] != i:
                tmp_order.append(order[j])

        for j in range(N):
            order[j] = tmp_order[j]
        
for i in order:
    print(i + 1, end=' ')