''' 방향 벡터 저장 딕셔너리 '''
dirs = {
    'R': (0, 1),    # 오른쪽
    'L': (0, -1),   # 왼쪽
    'B': (1, 0),    # 아래
    'T': (-1, 0),   # 위
    'RT': (-1, 1),  # 오른쪽 위 대각선
    'LT': (-1, -1), # 왼쪽 위 대각선
    'RB': (1, 1),   # 오른쪽 아래 대각선
    'LB': (1, -1)   # 왼쪽 아래 대각선
}

# 킹의 위치, 돌의 위치, 움직이는 횟수
king, stone, N = input().split()

# 인덱스 1부터 8까지
N = int(N)
ky, kx = 9 - int(king[1]), ord(king[0]) - 64    # A 좌표: 1
sy, sx = 9 - int(stone[1]), ord(stone[0]) - 64

board = [[0] * 9 for _ in range(9)]

KING = 1
STONE = 2

# 입력으로 주어진 초기 왕과 돌 위치 초기화
board[ky][kx] = KING
board[sy][sx] = STONE

for _ in range(N):
    d = input() # 움직이는 정보

    # 왕의 다음 위치
    kny = ky + dirs[d][0]
    knx = kx + dirs[d][1]

    # 1. 왕이 보드 밖으로 나가면, 해당 이동 건너뛰기
    if not (0 < kny < 9 and 0 < knx < 9):
        continue

    # 2. 왕의 다음 위치가 돌의 위치라면, 돌을 왕이 움직이는 방향으로 한 칸 옮김
    if kny == sy and knx == sx:
        sny = sy + dirs[d][0]
        snx = sx + dirs[d][1]

        # 2-1. 돌이 보드 밖으로 나가면, 해당 이동 건너뛰기
        if not (0 < sny < 9 and 0 < snx < 9):
            continue
        
        # 2-2. 돌이 나가지 않았으면, 왕과 돌을 옮김
        board[ky][kx] = 0
        board[kny][knx] = KING
        board[sny][snx] = STONE

        # 다 옮기고, 옮긴 위치를 현재 위치로 갱신한다.
        ky, kx = kny, knx
        sy, sx = sny, snx

    # 3. 왕의 다음 위치가 돌이 아니면, 왕만 옮긴다.
    else:
        board[ky][kx] = 0
        board[kny][knx] = KING

        ky, kx = kny, knx

# for i in range(9):
#     for j in range(9):
#         print(board[i][j], end=' ')
#     print()

for i in range(9):
    for j in range(9):
        # 체스식 좌표로 변환
        if board[i][j] == KING:
            ky = 9 - i
            kx = chr(j + 64)
        if board[i][j] == STONE:
            sy = 9 - i
            sx = chr(j + 64)

# 열, 행 순으로 출력
print(f'{kx}{ky}')
print(f'{sx}{sy}')