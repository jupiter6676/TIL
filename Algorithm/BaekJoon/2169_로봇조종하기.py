import sys
input = sys.stdin.readline

def pprint(mat):
    print('=================')
    for row in mat:
        for elem in row:
            print(elem, end=' ')
        print()

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[int(-1e9)] * M for _ in range(N)]

dp[0][0] = graph[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j - 1] + graph[0][j]

for i in range(1, N):
    left = dp[i][:]     # 왼쪽으로 이동하는 경우
    right = dp[i][:]    # 오른쪽으로 이동하는 경우

    # 왼쪽으로 이동
    for j in range(M - 1, -1, -1):
        if j == M - 1:
            left[j] = dp[i - 1][j] + graph[i][j]
        else:   # 위에서 내려오거나, 오른쪽에서 왼쪽으로 이동하는 것 중 더 큰 가치
            left[j] = max(dp[i - 1][j], left[j + 1]) + graph[i][j]

    # 오른쪽으로 이동
    for j in range(M):
        if j == 0:
            right[j] = dp[i - 1][j] + graph[i][j]
        else:   # 위에서 내려오거나, 왼쪽에서 오른쪽으로 이동하는 것 중 더 큰 가치
            right[j] = max(dp[i - 1][j], right[j - 1]) + graph[i][j]

    # 각 칸에 대해, 둘 중 더 큰 가치를 저장
    for j in range(M):
        dp[i][j] = max(left[j], right[j])

# pprint(dp)
print(dp[N - 1][M - 1])

'''
5 5
-100 -100 -100 -100 -100
-100 -100 -100 -100 -100
-100 -100 -100 -100 -100
-100 -100 -100 -100 -100
-100 -100 -100 -100 -100
답: -900

3 3
1 1 -9
-9 1 -9
-9 1 1
답: 5
'''