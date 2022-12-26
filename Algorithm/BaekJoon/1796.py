def recursion(X, depth):
    if len(X) == 1:
        print(depth)
        
        if int(X) % 3 == 0:
            print('YES')
        else:
            print('NO')
        return
    
    Y = 0
    for digit in X:
        Y += int(digit)

    recursion(str(Y), depth + 1)


N = input()
recursion(N, 0)