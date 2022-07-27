s = input()
cnt = 0

i = 0   # index
croatia_len = len(s)    # 크로아티아 알파벳을 고려한 문자열의 길이

while i < len(s) - 1:
    if s[i] == 'c':
        if s[i + 1] == '=' or s[i + 1] == '-':
            i += 1  # 뒤로 한 칸만 이동 (마지막에 무조건 한 칸 더 이동하기 때문에)
            croatia_len -= 1

    elif s[i] == 'd':
        if s[i + 1] == '-':
            i += 1
            croatia_len -= 1
        # d의 두 칸 뒤까지 검사
        # 두 칸 뒤가 문자열 범위를 넘어서지 않고,
        # d 다음이 z이고, 다다음이 = 일 때
        elif i + 2 < len(s) and (s[i + 1] == 'z' and s[i + 2] == '='):
            i += 2
            croatia_len -= 2    # 길이에서 -2

    elif s[i] == 'l':
        if s[i + 1] == 'j':
            i += 1
            croatia_len -= 1

    elif s[i] == 'n':
        if s[i + 1] == 'j':
            i += 1
            croatia_len -= 1

    elif s[i] == 's':
        if s[i + 1] == '=':
            i += 1
            croatia_len -= 1

    elif s[i] == 'z':
        if s[i + 1] == '=':
            i += 1
            croatia_len -= 1

    i += 1

print(croatia_len)