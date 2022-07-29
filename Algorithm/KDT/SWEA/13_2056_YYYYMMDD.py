def is_valid(m, d):
    flag = True
    m = int(m)
    d = int(d)

    if m < 1 or m > 12:
        flag = False
    else:
        if m == 2 and d > 28:
            flag = False
        if m == 4 or m == 6 or m == 9 or m == 11:
            if d > 30:
                flag = False

    return flag

T = int(input())
for test_case in range(1, T + 1):
    s = input()
    y = s[:4]
    m = s[4:6]
    d = s[6:8]

    print(f'#{test_case}', end=' ')
    if is_valid(m, d):
        print(f'{y}/{m}/{d}')
    else:
        print('-1')