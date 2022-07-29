s = input()
# print(s.upper())
for ch in s:
    if 97 <= ord(ch) <= 122:
        print(chr(ord(ch) - 32), end='')
    else:
        print(ch, end='')