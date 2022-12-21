def solution():
    if len(seq) == M:
        print(*seq)
        return
    
    for i in range(len(lst)):
        seq.append(lst[i])
        solution()
        seq.pop()


'''main'''
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
seq = list()

solution()