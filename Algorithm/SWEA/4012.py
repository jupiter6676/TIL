import sys
sys.stdin = open('input.txt', 'r')

'''
1
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
'''

def recursion(start):
    global min_diff

    if len(tmp_a) == N // 2:
        tmp_b = list(total - set(tmp_a))
        # print(tmp_a, tmp_b)

        sum_a = 0
        sum_b = 0
        for i in range(N // 2):
            for j in range(N // 2):
                if i != j:
                    sum_a += S[tmp_a[i]][tmp_a[j]]
                    sum_b += S[tmp_b[i]][tmp_b[j]]

        min_diff = min(min_diff, abs(sum_a - sum_b))

        return

    for i in range(start, N):
        tmp_a.append(i)
        recursion(i + 1)
        tmp_a.pop()


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    total = {i for i in range(N)}   # 총 식재료 종류
    tmp_a = list()  # A음식에 들어가는 식재료
    min_diff = 9999999999

    recursion(0)
    print(f'#{t} {min_diff}')