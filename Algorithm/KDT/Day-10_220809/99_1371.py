# import sys
# sys.stdin = open("input.txt")

alpha = dict()

while True:
    try:
        string = input()

        for ch in string:
            if 97 <= ord(ch) <= 122:
                alpha[ch] = alpha.get(ch, 0) + 1

    except:
        break

alpha = sorted(alpha.items(), key=lambda x: (-x[1], x[0]))

max_value = alpha[0][1]

for k, v in alpha:
    if v == max_value:
        print(k, end='')
    else:
        break