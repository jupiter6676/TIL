def minmax(x):
    min_x = ''
    max_x = ''

    for digit in x:
        if digit == '5':
            min_x += digit
            max_x += '6'

        elif digit == '6':
            min_x += '5'
            max_x += digit

        else:
            min_x += digit
            max_x += digit

    return int(min_x), int(max_x)


a, b = input().split()

min_ab = minmax(a)[0] + minmax(b)[0]
max_ab = minmax(a)[1] + minmax(b)[1]

print(min_ab, max_ab)