import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def pprint(mat):
    print('===========')
    for row in mat:
        for elem in row:
            print('%2d' % elem, end=' ')
        print()

# Top down
def cut(l, r, k):
    if l > r:
        return 0
    
    if dp[l][r]:
        return dp[l][r]
    
    # 1. k번째에 왼쪽 벼를 잘랐을 때 + (l + 1) ~ r번째 벼가 남았을 때의 최대 수확
    left_cut = v[l] * k + cut(l + 1, r, k + 1)

    # 2. k번째에 오른쪽 벼를 잘랐을 때 + l ~ (r - 1)번째 벼가 남았을 때의 최대 수확
    right_cut = cut(l, r - 1, k + 1) + v[r] * k

    dp[l][r] = max(left_cut, right_cut) # 왼쪽 벼나 오른쪽 벼를 잘랐을 때, 더 큰 값 저장

    return dp[l][r]


'''main'''
N = int(input())
v = list()
for _ in range(N):
    v.append(int(input()))

# dp[i][j]: i번째 ~ j번째 벼가 남아있는 상태에서, 그때까지 저장된 최대 수확량
dp = [[0] * N for _ in range(N)]

cut(0, N - 1, 1)
print(dp[0][N - 1])