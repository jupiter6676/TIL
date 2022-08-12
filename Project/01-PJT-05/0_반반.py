import sys

sys.stdin = open("_반반.txt")

T = int(input())

for tc in range(1, T + 1):
    S = input()
    dic = dict()

    for ch in S:
        dic[ch] = dic.get(ch, 0) + 1

    print(f'#{tc}', end=' ')
    
    if len(dic) == 2:
        for k, v in dic.items():
            if v != 2:
                print('No')
                break
        else:
            print('Yes')
    else:
        print('No')