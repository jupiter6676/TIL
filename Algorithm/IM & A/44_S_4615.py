T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())    # 보드 한 변, 돌 놓는 횟수
    board = [[0] * N for _ in range(N)]

    BLACK = 1
    WHITE = 2

    board[N//2 - 1][N//2 - 1] = WHITE
    board[N//2 - 1][N//2] = BLACK
    board[N//2][N//2 - 1] = BLACK
    board[N//2][N//2] = WHITE

    for _ in range(M):
        x, y, stone = map(int, input().split())
        x -= 1
        y -= 1

        board[y][x] = stone

        #
        dy = [-1, -1, -1, 0, 1, 1, 1, 0]
        dx = [-1, 0, 1, 1, 1, 0, -1, -1]

        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]

            visited = list()   # 이미 뒤집힌 돌은 뒤집지 않도록

            # if not (0 <= ny < N and 0 <= nx < N):
            #     continue

            # 자신의 색과 다른 돌을 만나면
            # if board[ny][nx] != 0 and board[ny][nx] != stone:
                # 계속 그 방향으로 전진
            while True:
                if not (0 <= ny < N and 0 <= nx < N):
                    visited = list()
                    break

                if board[ny][nx] == 0:
                    visited = list()
                    break

                if board[ny][nx] == stone:
                    for elem in visited:
                        if stone == WHITE:
                            board[elem[0]][elem[1]] = WHITE
                        else:
                            board[elem[0]][elem[1]] = BLACK

                    break

                else:
                    visited.append([ny, nx])

                ny += dy[d]
                nx += dx[d]
                    
        # for row in board:
        #     for elem in row:
        #         print(elem, end=" ")
        #     print()
        # print("---------------------------")

    black_cnt = 0
    white_cnt = 0

    for row in board:
        for elem in row:
            if elem == BLACK:
                black_cnt += 1
            elif elem == WHITE:
                white_cnt += 1

    print(f'#{t} {black_cnt} {white_cnt}')




'''
1
4 12 
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''