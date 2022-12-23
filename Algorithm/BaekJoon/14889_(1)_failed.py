import time
start = time.time()  # 시작 시간 저장

def recursion():
    global min_diff

    if len(tmp_seq) == N:
        # 반반씩 나누어 팀 나누기
        team_start = tmp_seq[: N//2]
        team_link = tmp_seq[N//2 :]

        sum_start = 0
        for i in team_start:
            for j in team_start:
                if i != j:
                    sum_start += S[i][j]
        
        sum_link = 0
        for i in team_link:
            for j in team_link:
                if i != j:
                    sum_link += S[i][j]

        diff = abs(sum_start - sum_link)
        min_diff = min(min_diff, diff)
        return

    for i in range(N):
        if not i in tmp_seq:
            tmp_seq.append(i)
            recursion()
            tmp_seq.pop()


'''main'''
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_diff = 9999
tmp_seq = list()    # N명의 수열 → 반반씩 나누기

recursion()
print(min_diff)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간