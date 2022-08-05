from collections import deque
import sys

sys.stdin = open("_암호생성기.txt")

while True:
    # 테스트 케이스가 몇 개인지 모르겠어서
    # EOFError 시 종료하도록..
    try:
        test_case = int(input())
        code = deque(map(int, input().split()))

        is_end = False

        while True:
            if is_end:
                break
            
            # Cycle
            for i in range(1, 6):
                # 맨 뒤가 0이 되면 반복 종료
                if code[-1] == 0:
                    is_end = True
                    break
                
                pop = code.popleft() - i

                # i를 뺀 게 0보다 작으면 0으로
                if pop <= 0:
                    pop = 0

                code.append(pop)

        print(f'#{test_case}', end=' ')
        print(*list(code))

    except EOFError:
        break