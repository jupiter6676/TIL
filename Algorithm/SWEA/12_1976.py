T = int(input())

for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())

    if m1 + m2 < 60:
        H = (h1 + h2) % 12
        M = m1 + m2

    else:
        H = (h1 + h2 + 1) % 12
        M = (m1 + m2) % 60

    if H == 0:
        H = 12  # H는 1 ~ 12사이 정수

    print(f'#{test_case} {H} {M}')