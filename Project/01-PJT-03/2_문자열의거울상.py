import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for test_case in range(1, T + 1):
    s = input()
    mirrored_s = ''

    # 거울이니까 거꾸로 탐색
    for ch in s[::-1]:
        if ch == 'b':
            mirrored_s += 'd'
        elif ch == 'd':
            mirrored_s += 'b'
        elif ch == 'p':
            mirrored_s += 'q'
        else:
            mirrored_s += 'p'

    print(f'#{test_case} {mirrored_s}')