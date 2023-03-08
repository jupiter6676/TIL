import sys
input = sys.stdin.readline

string = input().rstrip()       # 1,000,000
bomb = list(input().rstrip())   # 36
bomb_len = len(bomb)

stack = list()
for ch in string:
    stack.append(ch)

    # 폭발 문자열의 마지막 문자와 같으면
    # 스택에서 폭발 문자열의 길이만큼 비교
    if ch == bomb[-1] and stack[-bomb_len:] == bomb:
        # stack = stack[:-bomb_len]
        for _ in range(bomb_len):
            stack.pop()
        
if stack:
    print(*stack, sep='')
else:
    print('FRULA')