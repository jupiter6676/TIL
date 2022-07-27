T = int(input())

for t in range(T):
    pos, s = input().split()

    correct_s = ''

    for i in range(len(s)):
        # 오타가 아닐 때만 글자 이어붙이기
        if i != int(pos) - 1:
            correct_s += s[i]

    print(correct_s)