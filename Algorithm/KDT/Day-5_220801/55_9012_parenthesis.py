T = int(input())

for test_case in range(T):
    ps = list(input())    # Parenthesis String
    is_valid = True

    stack = list()

    # 괄호 문자열 순회
    for p in ps:
        # 열린 괄호는 스택에 push
        if p == '(':
            stack.append(p)

        # 닫힌 괄호는
        if p == ')':
            # 스택에 원소가 있을 때
            # = 열린 괄호가 있을 때, 그걸 pop
            if stack:
                stack.pop()
            # 스택이 비어있을 때
            # 열린 괄호가 없는데 닫힌 괄호가 왔다면 VPS가 아님
            # is_valid = False
            else:
                is_valid = False
                break
    # 다 순회했는데, 스택이 비어있지 않다면,
    # 즉 열린 괄호가 남아 다 닫히지 않았다면
    # is_valid = False
    if stack:
        is_valid = False
   
    print('YES' if is_valid else 'NO')