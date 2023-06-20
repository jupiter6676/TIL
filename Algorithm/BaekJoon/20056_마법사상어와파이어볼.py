# https://jennnn.tistory.com/77
import sys
input = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
balls = list()

for _ in range(M):
    # 위치 (y, x), 질량 m, 속력 s, 방향 d
    y, x, m, s, d = map(int, input().split())
    balls.append([y - 1, x - 1, m, s, d])

for _ in range(K):
    # 1. 모든 파이어볼 이동
    while balls:
        y, x, m, s, d = balls.pop()

        ny = (y + dy[d] * s) % N    # 1-N 행이 연결
        nx = (x + dx[d] * s) % N    # 1-N 열이 연결
        
        graph[ny][nx].append([m, s, d])

    # 2. 2개 이상 체크
    for y in range(N):
        for x in range(N):
            cnt = len(graph[y][x]) # 총 파이어볼의 개수

            # 1. 1개인 경우, 스택에 넣기
            if cnt == 1:
                balls.append([y, x] + graph[y][x].pop())

            # 2. 2개 이상인 경우, 4개로 쪼개기
            if cnt > 1:
                sum_m = sum_s = 0
                odd = even = 0  # 방향(d) 중 홀, 짝의 개수

                while graph[y][x]:
                    m, s, d = graph[y][x].pop()
                    sum_m += m
                    sum_s += s

                    if d % 2:
                        odd += 1
                    else:
                        even += 1

                if odd == cnt or even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                if sum_m // 5:
                    for d in nd:
                        balls.append([y, x, sum_m // 5, sum_s // cnt, d])

print(sum([ball[2] for ball in balls]))