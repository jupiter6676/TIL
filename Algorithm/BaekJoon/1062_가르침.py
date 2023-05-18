import sys
input = sys.stdin.readline

def check():
    global res

    cnt = 0
    for word in words:
        for c in word:
            # 단어를 이루는 글자를 배우지 않았으면 카운트 X
            if alpha[ord(c) - 97] == 0:
                break

        else:
            cnt += 1

    res = max(res, cnt)
    return


def dfs(start, depth):
    # K - 5개의 글자를 배웠을 때
    if K - 5 <= len(total_chars) and depth == K - 5:
        check()
        return
    
    # 혹은 배워야할 글자를 배웠을 때
    elif depth == len(total_chars):
        check()
        return
    
    # 글자 가르치기
    for i in range(start, len(total_chars)):
        c = ord(total_chars[i]) - 97
        if alpha[c]:
            continue

        alpha[c] = 1
        dfs(i + 1, depth + 1)
        alpha[c] = 0


'''main'''
N, K = map(int, input().split())
words = [input().rstrip()[4 : -4] for _ in range(N)]    # 시작과 끝 고정

if K < 5:   # 최소 a, c, i, n, t는 알아야 읽는다.
    print(0)

else:
    alpha = [0] * 26    # 알파벳을 배웠을 때 true
    for c in {'a', 'c', 'i', 'n', 't'}:
        alpha[ord(c) - 97] = 1

    total_chars = set()    # 단어를 이루는 모든 글자
    for word in words:
        for c in word:
            total_chars.add(c)
    total_chars = list(total_chars - {'a', 'c', 'i', 'n', 't'})

    res = 0
    dfs(0, 0)
    print(res)

'''
2 15
antabtica
antatica
답: 2
'''