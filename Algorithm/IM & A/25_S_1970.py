T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lst = [0] * 8

    lst[0] = N // 50000
    N %= 50000

    lst[1] = N // 10000
    N %= 10000

    lst[2] = N // 5000
    N %= 5000

    lst[3] = N // 1000
    N %= 1000

    lst[4] = N // 500
    N %= 500

    lst[5] = N // 100
    N %= 100

    lst[6] = N // 50
    N %= 50

    lst[7] = N // 10

    print(f'#{t}')
    print(*lst)