def rev(x):
    rev_arr = list()

    while x > 0:
        rev_arr.append(x % 10)
        x //= 10

    rev_num = 0
    for i in range(len(rev_arr)):
        digit_for_i = len(rev_arr) - (i + 1)
        rev_num += rev_arr[i] * (10 ** digit_for_i)

    return rev_num

x, y = map(int, input().split())
res = rev(rev(x) + rev(y))
print(res)