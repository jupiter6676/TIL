n = int(input())

for i in range(1, n + 1):
    i_toStr = str(i)
    
    cnt = 0

    for j in i_toStr:
        if j == '3' or j == '6' or j == '9':
            cnt += 1
        
    if cnt > 0:
        print('X' * cnt, end='')
    else:
        print(i, end='')
    
    print(end=' ')