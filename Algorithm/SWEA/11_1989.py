T = int(input())

for test_case in range(1, T + 1):
    stack = list()
    string = input()

    # 스택에 문자 넣기
    for ch in string:
        stack.append(ch)
    
    # 문자 하나씩 꺼내기
    for ch in string:
        pop = stack.pop()

        if ch != pop:
            print(f'#{test_case} 0')
            break

    else:
        print(f'#{test_case} 1')