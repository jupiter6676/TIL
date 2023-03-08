import sys
import heapq

input = sys.stdin.readline

N = int(input())
q = list()

for _ in range(N):
    heapq.heappush(q, int(input()))

res = 0
while len(q) >= 2:
    num1 = heapq.heappop(q)
    num2 = heapq.heappop(q)

    sum_ = num1 + num2
    res += sum_

    heapq.heappush(q, sum_)

    # print(res, q)

print(res)

'''
4
5
7
6
8

답: 52
'''