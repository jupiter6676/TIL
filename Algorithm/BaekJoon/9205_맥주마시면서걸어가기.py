import sys
from collections import deque
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def bfs(px, py):
    q = deque()
    q.append([px, py])
    visited = set()

    while q:
        x, y = q.popleft()

        if dist(x, y, end_x, end_y) <= 1000:
            return True

        for i in range(N):  # 편의점 순회
            store_x, store_y = stores[i]

            if (store_x, store_y) not in visited:   # 와 이게 되네
                if dist(x, y, store_x, store_y) <= 1000:
                    q.append([store_x, store_y])
                    visited.add((store_x, store_y))

    return False


'''main'''
T = int(input())
for _ in range(T):
    N = int(input())    # 편의점 개수
    start_x, start_y = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(N)]
    end_x, end_y = map(int, input().split())

    if bfs(start_x, start_y):
        print('happy')
    else:
        print('sad')