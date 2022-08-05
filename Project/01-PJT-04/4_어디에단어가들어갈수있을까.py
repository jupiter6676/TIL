import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    # 가로
    for i in range(N):
        tmp = 0

        for j in range(N):
            # 가로로 이동하면서, 
            # 흰 칸을 연속적으로 발견할 때마다 tmp +1
            if lst[i][j] == 1:
                tmp += 1

            # 검은 칸, 혹은 행의 끝을 만나면
            if lst[i][j] == 0 or j == N - 1:
                # 흰 칸의 수와 글자 수 K가 같은지 검사
                if tmp == K:
                    cnt += 1
                tmp = 0 # tmp 초기화

    # 세로
    for j in range(N):
        tmp = 0
        for i in range(N):
            if lst[i][j] == 1:
                tmp += 1

            if lst[i][j] == 0 or i == N - 1:
                if tmp == K:
                    cnt += 1
                tmp = 0

    print(f'#{test_case} {cnt}')