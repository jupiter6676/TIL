from collections import deque

# 총 F층, 처음 위치 S층, 목표 G층, 엘리베이터 위로 U층, 아래로 D층
F, S, G, U, D = map(int, input().split())   # 100 100 1 1 100
stairs = [0] * (F + 1)  # 건물은 1층부터
q = deque()
dx = [U, -D]

stairs[S] = 1
q.append(S)

if S == G:
    print(0)

else:
    while q:
        x = q.popleft()
        
        for d in range(2):
            nx = x + dx[d]

            if not (0 < nx < F + 1):
                continue
            
            if stairs[nx] == 0:
                stairs[nx] = stairs[x] + 1
                q.append(nx)

    if stairs[G] == 0:
        print('use the stairs')
    else:
        print(stairs[G] - 1)