def solution(start):
    if len(seq) == M:
        print(*seq)
        return

    for i in range(start, N + 1):
        if not i in seq:
            seq.append(i)
            solution(i + 1)
            seq.pop()
                


'''main'''
N, M = map(int, input().split())
seq = list()

solution(1)