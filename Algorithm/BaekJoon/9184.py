'''
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b < c:
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
'''

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 이미 저장된 값이면, 재귀호출 X
    elif dp[a][b][c]:
        return dp[a][b][c]

    # 1. 새로 저장 (1)
    elif a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    
    # 2. 새로 저장 (2)
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    
    return dp[a][b][c]



while True:
    A, B, C = map(int, input().split())
    dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

    if A == -1 and B == -1 and C == -1:
        break

    print(f'w({A}, {B}, {C}) = {w(A, B, C)}')