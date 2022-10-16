from pprint import pprint


T = int(input())

# R B W의 모든 경우의 수를 구한 다음 → i
# 각 경우에 해당하는 R B W의 줄 수를 구하기 → colors[i][0] ~ colors[i] ~ 3
# 총 i * 3의 반복문 돌기?

for t in range(1, T + 1):
    N, M = map(int, input().split())    # 행, 열의 개수
    graph = [[''] * M for _ in range(N)]    # 입력과 상하 반전된 그래프
    new_graph = [[''] * M for _ in range(N)]    # 러시아 국기
    
    # 원래 입력의 그래프를 상하 반전시킨 그래프
    for i in range(N - 1, -1, -1):
        graph[i] = list(input())


    colors = [0] * 3    # R, B, W가 총 몇 줄 있어야 하는지 저장

    # R, B, W 색상의 칸 개수
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                colors[0] += 1
            elif graph[i][j] == 'B':
                colors[1] += 1
            else:
                colors[2] += 1

    # R, B, W의 필요한 줄 수 구하기
    for i in range(3):
        # 만약 색이 하나도 없으면, 적어도 한 줄 채워주기
        if colors[i] == 0:
            colors = 1
            
        elif colors[i] % M != 0:
            colors[i] = colors[i] // M + 1
    
    cnt = 0
    for i in range(colors[0]):
        for j in range(M):
            new_graph[i][j] = 'R'
            
            if graph[i][j] != new_graph[i][j]:
                cnt += 1


    for i in range(colors[0], colors[0] + colors[1]):
        for j in range(M):
            new_graph[i][j] = 'B'

            if graph[i][j] != new_graph[i][j]:
                cnt += 1

    for i in range(colors[0] + colors[1], colors[1] + colors[2]):
        if i >= N:
            break

        for j in range(M):
            new_graph[i][j] = 'W'

            if graph[i][j] != new_graph[i][j]:
                cnt += 1

    print(f'#{t} {cnt}')
            

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