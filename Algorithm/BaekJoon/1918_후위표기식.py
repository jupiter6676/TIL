inorder = input()
stack = list()

for i in range(len(inorder)):
    if inorder[i] == '(':
        stack.append(inorder[i])

    # 열린 괄호 나올 때까지 pop
    elif inorder[i] == ')':
        while stack[-1] != '(':
            print(stack.pop(), end='')

        stack.pop()
    
    elif inorder[i] in '*/':
        # 우선순위가 같은 *, /가 먼저 나왔다면, 그걸 모두 출력
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(), end='')
        
        stack.append(inorder[i])

    elif inorder[i] in '+-':
        # 우선순위가 더 높은 (, *, /을 출력(열린 괄호 제외)
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')

        stack.append(inorder[i])

    else:
        print(inorder[i], end='')

while stack:
    print(stack.pop(), end='')

'''
G*(A-B*(C/D+E)/F)
답: GABCD/E+*F/-*
'''