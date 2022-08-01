'''시간 초과'''

N, M = map(int, input().split())

flag = True

# 총 M개의, 각 더미의 정보
for _ in range(M):
    m = int(input())    # 한 더미의 책 권수

    # m권의 책 번호 ki 입력
    stack = list(map(int, input().split()))
    
    max_k = 0

    while len(stack):
        pop = stack.pop()
        
        if pop > max_k:
            max_k = pop

        if pop < max_k:
            flag = False
            break

if flag:
    print('Yes')
else:
    print('No')