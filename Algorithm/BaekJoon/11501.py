T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    res = 0

    max_ = 0
    for i in range(N - 1, -1, -1):  # 뒤에서부터 순회
        if nums[i] > max_:  # 현재의 가격이 지금까지의 가장 비쌀 때보다 크다면
            max_ = nums[i]  # 값을 갱신하고 다시 res에 더해나가기 (거꾸로 도니까)
        else:
            res += max_ - nums[i]

    print(res)


'''
6
1
1 2 3 2 4 1

답: 8
'''