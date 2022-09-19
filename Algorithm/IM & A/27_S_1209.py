import sys

sys.stdin = open('input.txt', 'r')


for _ in range(1, 11):
    t = int(input())    # test cast 번호
    lst = [list(map(int, input().split())) for _ in range(100)] # 100 X 100

    sum_lst = list()

    sum_d1 = 0  # 우하향 대각선의 합
    sum_d2 = 0  # 좌하향 대각선의 합

    for i in range(100):
        sum_r = 0   # 한 행의 합
        sum_c = 0   # 한 열의 합

        for j in range(100):
            sum_r += lst[i][j]
            sum_c += lst[j][i]

            if i == j:
                sum_d1 += lst[i][j]
            if 100 - i - 1 == j:
                sum_d2 += lst[i][j]

            sum_lst.append(sum_r)
            sum_lst.append(sum_c)

    sum_lst.append(sum_d1)
    sum_lst.append(sum_d2)

    print(f'#{t} {max(sum_lst)}')