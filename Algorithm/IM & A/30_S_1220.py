import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    K = int(input())
    graph = [list(map(int, input().split())) for _ in range(K)]

    # N극이 위에 있으니까
    # 빨간 자성체가 있으면, 아래로 내려간다. 파란 자성체를 만나면 교착상태 +1
    # 빨간 자성체를 만나거나 빈공간이 계속되면, 그대로 떨어짐

    N = 1   # N극(빨간) 자성체
    S = 2   # S극(파란) 자성체

    total = 0

    # 열부터 탐색
    for j in range(K):
        is_red = False

        for i in range(K):
            if graph[i][j] == N and not is_red:
                is_red = True
            
            if is_red and graph[i][j] == S:
                total += 1
                is_red = False

    print(f'#{t} {total}')