import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
for _ in range(N):
    word = input().rstrip()
    alpha_dic = dict()
    is_group_word = True

    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            if alpha_dic.get(word[i]):
                is_group_word = False
                break
            else:
                alpha_dic[word[i]] = 1

        if i == len(word) - 2:
            if alpha_dic.get(word[i + 1]):
                is_group_word = False
                break

    if is_group_word:
        cnt += 1

print(cnt)