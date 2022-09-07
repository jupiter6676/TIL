W, H = map(int, input().split())
N = int(input())    # 상점의 수

graph = list()  # 상점의 위치

for _ in range(N + 1):
    # 상점 방향, 거리 (WE-왼쪽, NS-위쪽)
    d, dist = map(int, input().split())

    # 북쪽
    if d == 1:
        graph.append((d, dist, H))
    # 남쪽
    elif d == 2:
        graph.append((d, dist, 0))
    # 서쪽
    elif d == 3:
        graph.append((d, 0, H - dist))
    # 동쪽
    else:
        graph.append((d, W, H - dist))

# 경비원의 위치
pos_ = graph.pop()

# print(graph)
# print(pos_)

total = 0

# 경비원이 북쪽
if pos_[0] == 1:
    for i in range(N):
        # 상점이 북쪽
        if graph[i][0] == 1:
            total += abs(pos_[1] - graph[i][1])
        # 상점이 서쪽/동쪽
        elif graph[i][0] == 3 or graph[i][0] == 4:
            diff_y = abs(pos_[2] - graph[i][2])
            diff_x = abs(pos_[1] - graph[i][1])
            total += diff_x + diff_y
        # 상점이 남쪽
        else:
            diff_y = H
            diff_x = min(pos_[1] + graph[i][1], 2 * W - pos_[1] - graph[i][1])
            total += diff_x + diff_y

# 경비원이 남쪽
elif pos_[0] == 2:
    for i in range(N):
        # 상점이 남쪽
        if graph[i][0] == 2:
            total += abs(pos_[1] - graph[i][1])
        # 상점이 서쪽/동쪽
        elif graph[i][0] == 3 or graph[i][0] == 4:
            diff_y = abs(pos_[2] - graph[i][2])
            diff_x = abs(pos_[1] - graph[i][1])
            total += diff_x + diff_y
        # 상점이 북쪽
        else:
            diff_y = H
            diff_x = min(pos_[1] + graph[i][1], 2 * W - pos_[1] - graph[i][1])
            total += diff_x + diff_y

# 경비원이 서쪽
elif pos_[0] == 3:
    for i in range(N):
        # 상점이 서쪽
        if graph[i][0] == 3:
            total += abs(pos_[2] - graph[i][2])
        # 상점이 북쪽/남쪽
        elif graph[i][0] == 1 or graph[i][0] == 2:
            diff_y = abs(pos_[2] - graph[i][2])
            diff_x = abs(pos_[1] - graph[i][1])
            total += diff_x + diff_y
        # 상점이 동쪽
        else:
            diff_y = min(pos_[2] + graph[i][2], 2 * H - pos_[2] - graph[i][2])
            diff_x = W
            total += diff_x + diff_y

# 경비원이 동쪽
elif pos_[0] == 4:
    for i in range(N):
        # 상점이 동쪽
        if graph[i][0] == 4:
            total += abs(pos_[2] - graph[i][2])
        # 상점이 북쪽/남쪽
        elif graph[i][0] == 1 or graph[i][0] == 2:
            diff_y = abs(pos_[2] - graph[i][2])
            diff_x = abs(pos_[1] - graph[i][1])
            total += diff_x + diff_y
        # 상점이 서쪽
        else:
            diff_y = min(pos_[2] + graph[i][2], 2 * H - pos_[2] - graph[i][2])
            diff_x = W
            total += diff_x + diff_y

print(total)

'''
10 5
1
3 2
4 2
'''