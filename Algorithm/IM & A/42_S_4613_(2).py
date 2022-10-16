T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())    # 행, 열의 개수
    graph = [list(input()) * M for _ in range(N)]    # 입력 그래프 (W B R 순)
    new_graph = [[''] * M for _ in range(N)]    # 러시아 국기


    white = [0] * N    # 각 행에 W가 몇 개인지
    blue = [0] * N    # 각 행에 B가 몇 개인지
    red = [0] * N    # 각 행에 R가 몇 개인지

    # W, B, R 색상의, 각 행의 칸 개수
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'W':
                white[i] += 1
            elif graph[i][j] == 'B':
                blue[i] += 1
            else:
                red[i] += 1


    res = N * M # 새로 칠해야 하는 칸의 수는 최대 N * M개

    # 맨 첫 줄과 맨 아랫 줄은 R, W로 고정. 그 중간에는 B
    # R은 최소 0, 최대 N - 3번째 줄 (N - 2번째 줄 B, N - 1번째 줄 W)
    for w in range(0, N - 2):
        # W는 최대 N - 1, 최소 r + 2번째 줄 (r + 1부터는 B가 최소 한 줄 필요)
        for r in range(N - 1, w + 1, -1):
            keep = 0    # 새로 칠하지 않아도 되는 칸의 수

            for i in range(N):
                if i <= w:
                    keep += white[i]
                
                elif i >= r:
                    keep += red[i]
                
                # B는 r + 1부터 w - 1까지
                else:
                    keep += blue[i]

            res = min(res, N * M - keep)

    print(f'#{t} {res}')
    


'''
1
4 5
WRWRW
BWRWB
WRWRW
RWBWR

1
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
'''