while True:
    s = input()
    stack = list()
    answer = 'yes'

    # 입력 종료 조건
    if s == '.':    break

    for ch in s:
        # 열린 괄호는 push
        if ch == '(' or ch == '[':
            stack.append(ch)

        # 닫힌 소괄호
        elif ch == ')':
            # 스택이 비어있으면
            if not stack:
                answer = 'no'

            # top이 열린 소괄호면 pop
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    answer = 'no'

        # 닫힌 대괄호
        elif ch == ']':
            # 스택이 비어있으면
            if not stack:
                answer = 'no'

            # top이 열린 대괄호면 pop
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    answer = 'no'
        
    if stack:
        answer = 'no'

    print(answer)