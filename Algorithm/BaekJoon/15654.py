def solution():
    if len(seq) == M:
        print(*seq)
        return

    for i in lst:
        if not i in seq:
            seq.append(i)
            solution()
            seq.pop()


'''main'''
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
seq = list()

solution()