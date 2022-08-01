stack = list()  # 문제를 담을 스택

while True:
    s = input()

    if s == '고무오리 디버깅 끝':
        break

    # 문제를 입력
    if s == '문제':
        stack.append(1) # 스택에 문제 추가
    # 고무오리를 입력
    elif s == '고무오리':
        # 풀 문제가 없으면, 문제 2개 추가
        if not stack:
            stack.append(1)
            stack.append(1)
        else:
            stack.pop()

# 문제를 모두 풀면
if not stack:
    print('고무오리야 사랑해')
else:
    print('힝구')