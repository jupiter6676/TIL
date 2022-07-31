T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))

    res = 0
    for num in lst:
        if num % 2 == 1:
            res += num

    print(f'#{test_case} {res}')