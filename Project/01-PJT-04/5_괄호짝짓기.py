import sys

sys.stdin = open("_괄호짝짓기.txt")

for test_case in range(1, 11):
    N = int(input())
    s = input()

    stack = list()
    is_valid = 1

    for ch in s:
        # ch가 열린 괄호면 스택에 push
        if ch in '([{<':
            stack.append(ch)

        # ch가 닫힌 소괄호이면,
        if ch == ')':
            # top에 있는 것이 열린 소괄호일 때
            # (= 쌍이 맞을 때)
            # 그 열린 소괄호를 스택에서 pop
            if stack[-1] == '(':
                stack.pop()
            # 쌍이 맞지 않는 다른 괄호가 나온다면,
            # 그것은 invalid
            else:
                is_valid = 0
                break

        elif ch == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                is_valid = 0
                break
        
        elif ch == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                is_valid = 0
                break

        elif ch == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                is_valid = 0
                break

    # 반복문이 끝나고, 스택이 비어있지 않으면
    # (= 괄호가 열린 후 닫히지 않았으면)
    # invalid
    if stack:
        is_valid = 0

    print(f'#{test_case} {is_valid}')