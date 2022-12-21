def solution():
    if len(seq) == M:
        print(*seq)
        return

    # 4 2
    # 1 7 9 9
    # 9 → 9로 새로운 solution을 호출하면서, remember는 9 → 0이 되어, 새로운 9가 들어감
    # [9, 9]가 되어 그 solution 함수가 종료되면, 이전 9가 호출된 함수의 18번째 줄로 돌아옴
    # 그러면 remember는 9가 된다..
    remember = 0
    for i in range(N):
        if not visited[i] and remember != lst[i]:
            visited[i] = True
            seq.append(lst[i])
            remember = lst[i]
            solution()

            visited[i] = False
            seq.pop()


'''main'''
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False] * N   # lst[i] ↔ visited[i]
seq = list()

solution()