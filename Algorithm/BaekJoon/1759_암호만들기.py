import sys
input = sys.stdin.readline

def dfs(start):
    global seq

    if len(seq) == L:   # 최대 길이 15
        ch1 = False
        cnt = 0
        for c in seq:
            if c in 'aeiou':
                ch1 = True
            else:
                cnt += 1

            if ch1 and cnt >= 2:
                print(''.join(seq))
                return

    for i in range(start, C):
        seq.append(chars[i])
        dfs(i + 1)
        seq.pop()
    

L, C = map(int, input().split())
chars = list(input().split())
chars.sort()

seq = list()
dfs(0)

# 최소 한 개의 모음과 최소 두 개의 자음