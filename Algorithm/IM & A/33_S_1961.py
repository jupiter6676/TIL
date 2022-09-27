import sys
sys.stdin = open('input.txt', 'r')

'''
(0, 0) (0, 1) (0, 2)     (2, 0) (1, 0) (0, 0)
                         (0, 0) (0, 1) (0, 2) 

(1, 0) (1, 1) (1, 2)     (2, 1) (1, 1) (0, 1)
                         (1, 0) (1, 1) (1, 2)

(2, 0) (2, 1) (2, 2)     (2, 2) (1, 2) (0, 2)
                         (2, 0) (2, 1) (2, 2)
'''

# 시계방향으로 90도 회전
def rotate(matrix):
    rotated = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotated[i][j] = matrix[N - j - 1][i]

    return rotated


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [list(input().split()) for _ in range(N)] # 문자들이 요소
    
    rotate_90 = rotate(lst)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)

    print(f'#{t}')
    for i in range(N):
        print(''.join(rotate_90[i]), ''.join(rotate_180[i]), ''.join(rotate_270[i]))