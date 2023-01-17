import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

lines.sort()    # 시작 좌표를 기준으로 오름차순 정렬

start = lines[0][0]
end = lines[0][1]

total = 0
for i in range(1, N):
    # 1. 새로운 선분
    if end < lines[i][0]:
        total += end - start    # 이전 선분의 길이를 더함
        start = lines[i][0]     # start를 새로운 선분의 시작점으로 갱신
    
    # 2. 확장되는 선분
    if end < lines[i][1]:
        end = lines[i][1]       # end를 새로운 선분의 끝점으로 갱신

    # 3. 포함되는 선분 → 별도의 작업이 필요 X

total += end - start
print(total)


'''
4
5 10
15 20
25 30
7 35

30
'''