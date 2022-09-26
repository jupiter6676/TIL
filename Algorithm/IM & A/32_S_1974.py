import sys
sys.stdin = open('input.txt', 'r')

'''
1
7 3 6 4 8 9 2 5 1
8 5 2 7 3 1 6 9 4
9 1 4 5 6 2 7 3 8
4 9 7 2 5 6 8 1 3
5 6 3 1 8 7 9 4 2
2 8 1 9 4 3 5 6 7
6 7 5 3 2 4 1 8 9
1 4 9 6 7 8 3 2 5
3 2 8 1 9 5 4 7 6
'''

T = int(input())
for t in range(1, T + 1):
    graph = [list(map(int, input().split())) for _ in range(9)]

    is_valid = True

    # 가로 & 세로
    for i in range(9):
        col = list()

        for j in range(9):
            row = graph[i]
            col.append(graph[j][i])

        if len(set(row)) < 9 or len(set(col)) < 9:
            is_valid = False
            break
    
    # 3 X 3
    if is_valid:
        for i in range(9):
            for j in range(9):
                if (i == 0 or i == 3 or i == 6) and (j == 0 or j == 3 or j == 6):
                    submatrix = list()
                    for y in range(3):
                        for x in range(3):
                            submatrix.append(graph[i + y][j + x])

                    if len(set(submatrix)) < 9:
                        is_valid = False
                        break
    
    print(f'#{t}', end=' ')
    print(1 if is_valid else 0)