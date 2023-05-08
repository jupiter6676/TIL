import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chicks = list() # 모든 치킨집의 좌표
houses = list() # 모든 집의 좌표
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append([i, j])
        if graph[i][j] == 2:
            chicks.append([i, j])

m_chicks = list(combinations(chicks, M))   # M개의 치킨집 좌표
res = 9999
for coords in m_chicks:
    dists = dict() # 각 경우에서의 치킨 거리의 최솟값
    for y, x in houses:
        dists[(y, x)] = 9999

    for cy, cx in coords:
        for hy, hx in houses:
            dist = abs(cy - hy) + abs(cx - hx)
            dists[(hy, hx)] = min(dists[(hy, hx)], dist)

    res = min(res, sum(dists.values()))
    # print(dists)

print(res)