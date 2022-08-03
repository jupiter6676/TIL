N, M = map(int, input().split())

castle = [list(input()) for _ in range(N)]
row_list = [0] * N  # 경비가 아무도 없는 행 번호를 체크
col_list = [0] * M  # 경비가 아무도 없는 열 번호를 체크

for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row_list[i] = 1
            col_list[j] = 1

r_cnt = 0    # 경비가 아무도 없는 행의 수
for r in row_list:
    if r == 0:
        r_cnt += 1

c_cnt = 0    # 경비가 아무도 없는 열의 수
for c in col_list:
    if c == 0:
        c_cnt += 1

print(r_cnt if r_cnt >= c_cnt else c_cnt)