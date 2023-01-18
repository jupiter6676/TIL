import sys
import heapq    # 최소힙 (가장 작은 값이 맨 앞으로 온다.)

input = sys.stdin.readline

N = int(input())
lecs = [list(map(int, input().split())) for _ in range(N)]

lecs.sort()   # 시작 시간 기준 정렬

q = list()
heapq.heappush(q, lecs[0][1])   # 첫 번째 회의 종료 시간을 힙에 push

for i in range(1, N):
    # 현재 회의 종료 시간(q[0])보다, 다음 회의 시작 시간(lecs[i][0])이 빠르면
    if lecs[i][0] < q[0]:
        heapq.heappush(q, lecs[i][1])   # 새로운 강의실 개설 (다음 회의 종료 시간을 힙에 push)
    else:
        heapq.heappop(q)    # 다음 회의로 시간 변경을 위해 pop 후,
        heapq.heappush(q, lecs[i][1])   # 다음 회의의 종료 시간을 push

print(len(q))

'''
5
1 7
2 3
3 4
4 8
7 10

5
1 7
2 8
8 9
9 10
7 10


답 2
'''