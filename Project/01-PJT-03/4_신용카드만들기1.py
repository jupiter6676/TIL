import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for test_case in range(1, T + 1):
    card_nums = list(map(int, input().split()))

    sum_ = 0
    for i in range(len(card_nums)):
        # 홀수 자리(짝수 인덱스)의 수 → *2
        if i % 2 == 0:
            sum_ += card_nums[i] * 2

        # 짝수 자리(홀수 인덱스)의 수 → 그대로
        else:
            sum_ += card_nums[i]

    N = 0
    # N은 한 자리 수니까 0 ~ 9
    while N <= 9:
        if (sum_ + N) % 10 == 0:
            break
        N += 1

    print(f'#{test_case} {N}')