import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().split()))
M = int(input())

# dp[i][j]: i번째 수 ~ j번째 수가 팰린드롬인가
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i] = 1

    if nums[i - 1] == nums[i]:
        dp[i - 1][i] = 1    # 11, 22 이런 것도 팰린드롬

# 끝에서부터 돌기
for i in range(N, 0, -1):
    for j in range(N, i - 1, -1):
        if nums[i] != nums[j]:
            dp[i][j] = 0
        
        elif j + 1 <= N:
            # 오른쪽 위 대각선으로 값 옮기기
            # ex) nums[1] = nums[5] = 1 일 때,
            #     [1][5]가 팰린드롬인가?
            #     → [2][4]가 팰린드롬인가? (nums[2] = nums[4]면 O)
            #     → [3][3]가 팰린드롬인가? O
            dp[i - 1][j + 1] = dp[i][j]

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])

'''
2
1 1
1
1 2
답: 1
'''