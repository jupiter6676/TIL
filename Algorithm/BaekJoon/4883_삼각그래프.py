import sys
input = sys.stdin.readline

def pprint(mat):
    for row in mat:
        for elem in row:
            print(elem, end=' ')
        print()

T = 1
while True:
    N = int(input())

    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N)]

    dp[0][0] = 99999999
    dp[0][1] = graph[0][1]
    dp[0][2] = dp[0][1] + graph[0][2]
    
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][0]
        dp[i][1] = min(dp[i][0], min(dp[i - 1])) + graph[i][1]
        dp[i][2] = min(dp[i][1], dp[i - 1][1], dp[i - 1][2]) + graph[i][2]

    # print('=========')
    # pprint(dp)
    print(f'{T}. {dp[N - 1][1]}')
    T += 1

'''
2
13 7 5
7 13 6
0
답: 20

3
1 1 1
1 1 1
-1 1 1
0
답: 2

2
2 4 5
7 1 3
0
답: 5

2
-1 0 0
0 0 0
0
답: 0

2
13 7 5
15 6 16
0
답: 13

2
0 0 -1
0 -2 0
0
답: -3
'''