def solution(start):
    if len(seq) == M:
        print(*seq)
        return

    for i in range(start, N + 1):
        seq.append(i)
        solution(i)
        seq.pop()

'''main'''
N, M = map(int, input().split())
seq = list()

solution(1)