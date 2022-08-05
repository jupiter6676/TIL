import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_ = 0

    for i in range(N):
        for j in range(N):
            tmp = 0

            # 현재 위치에서, 가로 세로 + (m - 1)만큼
            # 즉, 가로 m, 세로 m의 직사각형 내의 합 구하기
            for dy in range(M):
                for dx in range(M):
                    # 배열의 인덱스 범위 내에서 합 구하기
                    if i + dy < N and j + dx < N:
                        tmp += lst[i + dy][j + dx]

                    # 합의 최댓값 갱신
                    if tmp > max_:
                        max_ = tmp

    print(f'#{test_case} {max_}')