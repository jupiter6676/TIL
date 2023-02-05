import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x: (x[0], -x[1]))    # 무게 오름차순, 가격 내림차순
bags.sort()

q = list()
res = 0
for i in range(K):
    # for j in range(N):
    #     if not visited[j] and bags[i] >= jewels[j][0]:
    #         heapq.heappush(q, -jewels[j][1])
    #         visited[j] = 1
    while jewels and jewels[0][0] <= bags[i]:
        heapq.heappush(q, -jewels[0][1])
        heapq.heappop(jewels)

    if q:
        res -= heapq.heappop(q)

print(res)

'''
4 2
4 100
5 110
6 90
7 80
5
7

답: 210


4 4
1 100
2 200
13 300
10 500
10
10
10
14

답: 1100

3 2
1 65
2 70
3 99
10
1

답: 164

6 3
1 65
1 50
2 70
3 90
4 80
7 20
1
5
10

답: 235
'''