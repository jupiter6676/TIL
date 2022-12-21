def solution():
    if len(seq) == M:
        # 중복 수열 체크
        if res.get(tuple(seq), 0) == 0:
            res[tuple(seq)] = 1
        return

    for i in range(len(lst)):
        if not visited[i]:
            seq.append(lst[i])
            visited[i] = True
            solution()

            seq.pop()
            visited[i] = False


'''main'''
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False] * N   # lst[i] ↔ visited[i]
seq = list()    # 길이 M의 리스트 (새로 만들어진 임시 수열)

# 키로 seq의 튜플 → 중복 수열 검사하는 딕셔너리
res = dict()

solution()

for seq in res.keys():
    print(*seq)