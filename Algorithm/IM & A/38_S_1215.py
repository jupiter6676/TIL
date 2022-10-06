import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())    # 회문의 길이
    graph = [list(input()) for _ in range(8)]

    p_cnt = 0

    # 1. 가로
    for i in range(8):
        # N은 1부터 시작하니까 -1
        for j in range(8 - (N - 1)):
            str_ = ''

            # 회문의 길이만큼
            for n in range(j, j + N):
                str_ += graph[i][n]
            
            if str_ == str_[::-1]:
                p_cnt += 1

    # 2. 세로
    for j in range(8):
        for i in range(8 - (N - 1)):
            str_ = ''

            for n in range(i, i + N):
                str_ += graph[n][j]
            
            if str_ == str_[::-1]:
                p_cnt += 1

    print(f'#{t} {p_cnt}')