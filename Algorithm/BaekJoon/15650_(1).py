def solution():
    if len(seq) == M:
        print(*seq)
        return

    for i in range(1, N + 1):
        if not i in seq:
            if not seq:
                seq.append(i)
                solution()
                seq.pop()

            elif i > max(seq):
                seq.append(i)
                solution()
                seq.pop()


'''main'''
N, M = map(int, input().split())
seq = list()

solution()