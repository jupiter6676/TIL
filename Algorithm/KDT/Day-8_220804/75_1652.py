'''
..XX..
자리 2개
'''

N = int(input())
room = [list(input()) for _ in range(N)]

tmp = 0
w_cnt = 0

# 가로로 누울 수 있는 자리
for i in range(N):
    for j in range(N):
        if room[i][j] == '.':
            tmp += 1

        # 짐이나 벽을 만났을 때
        if room[i][j] == 'X' or j == N - 1:
            # 공간이 2 이상이면
            if tmp >= 2:
                # 가로 자리 +1
                w_cnt += 1

            tmp = 0

tmp = 0
h_cnt = 0

# 세로로 누울 수 있는 자리
for j in range(N):
    for i in range(N):
        if room[i][j] == '.':
            tmp += 1
        
        if room[i][j] == 'X' or i == N - 1:
            if tmp >= 2:
                h_cnt += 1
            
            tmp = 0

print(w_cnt, h_cnt)