import sys
input = sys.stdin.readline

def pprint(mat):
    for row in mat:
        for elem in row:
            print(elem, end=' ')
        print()

N, M = map(int, input().split())

dp = [[0] * (M + 1)]  # (N + 1) × (M + 1)
for _ in range(N):
    row = [0] + list(map(int, input().rstrip()))
    dp.append(row)

res = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if dp[i][j] > 0:
            # (대각선 위, 위, 왼쪽)의 3군데 중 가장 작은 값 +1
            # → 해당 좌표까지의 가장 큰 정사각형의 한 변 길이 저장
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            
            res = max(res, dp[i][j])

# pprint(dp)
print(res ** 2) # 가장 큰 정사각형의 넓이

'''
1 1
1
답: 1

1 2
11
답: 1

2 1
1
1
답: 1

3 3
000
000
100
답: 1
'''