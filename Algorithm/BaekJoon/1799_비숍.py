# https://j2wooooo.tistory.com/80
import sys
input = sys.stdin.readline

def dfs(y, x, color, cnt):
    # 오른쪽으로 이동하다 줄을 넘긴 경우
    if x >= N:
        y += 1
        x = 1 if x % 2 == 0 else 0  # 다음 줄의 첫 시작 색을 설정

    # 모든 칸을 확인한 경우
    if y >= N:
        res[color] = max(res[color], cnt)
        return
    
    # 비숍을 놓을 수 있는 자리
    if graph[y][x] == 1:
        # 대각선 체크 → 우상향(y + x의 값이 같다), 우하향(y - x의 값이 같다)
        # 음수가 나오지 않도록 N - 1을 더해준다.
        if not pos[y + x] and not neg[y - x + N - 1]:
            graph[y][x] = 2 + color
            pos[y + x] = neg[y - x + N - 1] = True # 비숍 놓기
            dfs(y, x + 2, color, cnt + 1)   # 옆으로 2칸 이동

            # 비숍 빼기
            pos[y + x] = neg[y - x + N - 1] = False
            graph[y][x] = 1

    # 비숍을 놓지 않고 옆으로 2칸 이동
    dfs(y, x + 2, color, cnt)


'''main'''
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

pos = [False] * (N * 2) # 우상향 대각선 내 비숍 체크
neg = [False] * (N * 2) # 우하향 대각선 내 비숍 체크
res = [0] * 2   # 흰 칸, 검은 칸 비숍의 최대 개수

# 체스는 □, ■의 격자로 되어있다.
# → 흰 칸의 비숍과 검은 칸의 비숍은 서로 공격 X
# → 흰 칸에 놓을 수 있는 비숍, 검은 칸에 놓을 수 있는 비숍의 최대 개수를 각각 구한다.
dfs(0, 0, 0, 0) # 흰 칸
dfs(0, 1, 1, 0) # 검은 칸

# print(res)
print(sum(res))