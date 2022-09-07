def is_3_bingo(lst):
    bingo_cnt = 0

    # 가로줄 빙고 확인
    for i in range(5):
        tmp = 0
        for j in range(5):
            if lst[i][j] == -1:
                tmp += 1
            if tmp == 5:
                bingo_cnt += 1

    # 세로줄 빙고 확인
    for j in range(5):
        tmp = 0
        for i in range(5):
            if lst[i][j] == -1:
                tmp += 1
            if tmp == 5:
                bingo_cnt += 1

    # 대각선 빙고 확인
    tmp = 0
    for i in range(5):
        if lst[i][i] == -1:
            tmp += 1
        if tmp == 5:
            bingo_cnt += 1

    # 대각선 빙고 확인
    tmp = 0
    for i in range(5):
        if lst[i][4 - i] == -1:
            tmp += 1
        if tmp == 5:
            bingo_cnt += 1

    return True if bingo_cnt >= 3 else False


board = [list(map(int, input().split())) for _ in range(5)]
tmp_num = [list(map(int, input().split())) for _ in range(5)]

nums = list()
for i in range(5):
    for j in range(5):
        nums.append(tmp_num[i][j])

cnt = 0
game_end = False
for num in nums:
    if game_end:    break
    
    for i in range(5):
        if game_end:    break

        for j in range(5):
            if is_3_bingo(board):
                game_end = True
                break

            if board[i][j] == num:
                board[i][j] = -1

    cnt += 1

print(cnt)