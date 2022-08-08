T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    cnt = 0

    for i in range(N, M + 1):
        tmp = i

        if tmp == 0:
            cnt += 1
        else:
            while tmp > 0:
                if tmp % 10 == 0:
                    cnt += 1
                tmp //= 10

    print(cnt)