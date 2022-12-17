def solution():
    if len(seq) == M:
        print(*seq)
        return

    for n in range(1, N + 1):
        if not n in seq:    # 중복없이 숫자 선택
            seq.append(n)
            solution()
            seq.pop()
        
    return


'''main'''
N, M = map(int, input().split())
seq = list()

solution()