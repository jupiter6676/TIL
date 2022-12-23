# 오름차순으로 tmp_seq를 구성하기 위한 start 인자
# N // 2번의 재귀를 하기 위한 depth 인자
def recursion(start, depth):
    global min_diff

    # 1. 한 팀만 정하고, 나머지로 팀 구성
    if depth == N // 2:
        print(tmp_seq)
        team_start = tmp_seq[:]
        team_link = list(total - set(team_start))

        sum_start = 0     
        sum_link = 0
        for i in range(N // 2):
            for j in range(N // 2):
                if i != j:
                    sum_start += S[team_start[i]][team_start[j]]
                    sum_link += S[team_link[i]][team_link[j]]

        diff = abs(sum_start - sum_link)
        min_diff = min(min_diff, diff)

        return

    # 2. [1, 2], [2, 1]과 같은 중복 제거
    for i in range(start, N):
        tmp_seq.append(i)
        recursion(i + 1, depth + 1)
        tmp_seq.pop()


'''main'''
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_diff = 9999
total = {i for i in range(N)}   # N명의 선수를 차례로 나열한 전체 집합
tmp_seq = list()    # N // 2명의 수열

recursion(0, 0)
print(min_diff)