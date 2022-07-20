T = int(input())

for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())   # W: 한 달 사용 수도량

    # A사: 1리터 당 P원
    A = w * p

    # B사: R리터 까지는 기본 요금 Q, 초과량에 대해 1리터 당 S원
    B = q if w <= r else q + (w - r) * s

    if A < B:
        print(f'#{test_case} {A}')
    else:
        print(f'#{test_case} {B}')