import sys
input = sys.stdin.readline

N = int(input())
graph = [[0] * 1001 for _ in range(1001)]
area = [0] * (N + 1)

for p in range(1, N + 1):
    x1, y1, w, h = map(int, input().split())

    x2 = x1 + w
    y2 = y1 + h

    for i in range(y1, y2):
        for j in range(x1, x2):
            # 다른 색종이를 덮으면
            if graph[i][j] != p:
                # 해당 색종이의 면적을 -1
                area[graph[i][j]] -= 1
            
            # 색종이 깔기
            graph[i][j] = p
            area[graph[i][j]] += 1

# for i in range(min_y, max_y):
#     for j in range(min_x, max_x):
#         area[graph[i][j]] += 1

for i in range(1, len(area)):
    print(area[i])