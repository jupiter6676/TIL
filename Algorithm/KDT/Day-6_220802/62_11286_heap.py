import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = list()

for _ in range(N):
    x = int(input())

    # x = 0이면 가장 작은 수 출력
    if x == 0:
        if not heap:
            print(0)
        else:
            pop = heapq.heappop(heap)
            print(pop[1])

    # x != 0이면 힙에 (절댓값 x, x) 삽입
    else:
        heapq.heappush(heap,(abs(x), x))