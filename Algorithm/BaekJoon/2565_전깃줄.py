import sys
input = sys.stdin.readline

N = int(input())    # 전깃줄의 개수
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()

# 없애야 하는 전깃줄 수 = N - 없애지 않아도 되는 전깃줄 수
# → 왼쪽 위치 기준으로 정렬
# → ★ 재정렬된 오른쪽 위치 중, 가장 긴 증가하는 부분 수열을 구한다.
dp = [1] * N
for i in range(N):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(N - max(dp))

'''
10
1 6
2 8
3 2
4 9
5 5
6 10
7 4
8 1
9 7
10 3
답: 6
(7)
'''