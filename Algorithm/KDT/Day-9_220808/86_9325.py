T = int(input())

for test_case in range(T):
    s = int(input())    # 자동차 가격
    n = int(input())    # 옵션 개수

    sum_ = s
    for _ in range(n):
        q, p = map(int, input().split())
        sum_ += q * p

    print(sum_)