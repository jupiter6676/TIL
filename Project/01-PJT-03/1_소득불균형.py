import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    income = list(map(int, input().split()))

    # 평균 소득
    aver = sum(income) / N

    # 평균 소득 이하의 사람 수 세기
    cnt = 0
    for i in income:
        if i <= aver:
            cnt += 1

    print(f'#{test_case} {cnt}')