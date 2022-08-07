n = int(input())

for i in range(1, n + 1):
    cnt369 = 0

    for digit in str(i):
        if digit == '3' or digit == '6' or digit == '9':
            cnt369 += 1
    
    if cnt369:
        print('-' * cnt369, end='')
    else:
        print(i, end='')

    print(end=' ')