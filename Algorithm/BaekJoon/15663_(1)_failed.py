'''시간초과가 났지만 파이썬으로 2차원 배열 동적할당 하는 법'''
def solution():
    global res_idx

    if len(seq) == M:
        if not seq in res:
            # 2차원 리스트 동적할당
            res.append([])
            res[res_idx].extend(seq) # 리스트 끝에 iterable의 모든 항목 넣기
            res_idx += 1
        
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
seq = list()

# res: 2차원 리스트
res = list()
res_idx = 0 # 행의 인덱스

solution()

for row in res:
    print(*row)