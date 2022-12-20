def solution():
    if len(seq) == M:
        print(*seq)
        return

    for i in range(1, N + 1):
        if not seq:
            seq.append(i)
            solution()
            seq.pop()
        
        elif i >= seq[-1]:
            seq.append(i)
            solution()
            seq.pop()


'''main'''
N, M = map(int, input().split())
seq = list()

solution()