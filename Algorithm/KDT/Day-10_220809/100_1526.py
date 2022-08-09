N = int(input())

res = 0
for i in range(N, -1, -1):
    tmp = str(i)

    for digit in tmp:
        # if digit not in '47':
        ## if digit != '4' or digit != '7' 은 안 됨..
        if not (digit == '4' or digit == '7'):
            break
    else:
        res = tmp
        break

print(res)