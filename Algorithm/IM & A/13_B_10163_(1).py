N = int(input())
graph = [[0] * 1001 for _ in range(1001)]
area = [0] * (N + 1)

min_x = 9999
max_x = -9999

min_y = 9999
max_y = -9999

for p in range(1, N + 1):
    x1, y1, w, h = map(int, input().split())

    x2 = x1 + w
    y2 = y1 + h

    min_x = min(min_x, x1, x2)
    min_y = min(min_y, y1, y2)

    max_x = max(max_x, x1, x2)
    max_y = max(max_y, y1, y2)

    # 이중 반복문이랑 차이가 뭐지?
    # for i in range(y1, y2):
    #     for j in range(x1, x2):
    #         graph[i][j] = p

    for i in range(y1, y2):
        graph[i][x1 : x2] = [p] * w

# for i in range(min_y, max_y):
#     for j in range(min_x, max_x):
#         area[graph[i][j]] += 1

for i in range(min_y, max_y):
    for j in range(min_x, max_x):
        area[graph[i][j]] += 1

for i in range(1, len(area)):
    print(area[i])