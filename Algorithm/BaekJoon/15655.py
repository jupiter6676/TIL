def solution(start):
    if len(seq) == M:
        print(*seq)
        return

    for i in range(start, len(lst)):
        if not lst[i] in seq:
            seq.append(lst[i])
            solution(i)
            seq.pop()


'''main'''
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
seq = list()

solution(0)