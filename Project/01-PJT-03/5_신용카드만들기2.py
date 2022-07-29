import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for test_case in range(1, T + 1):
    # 하이픈은 지우고 리스트에 숫자 넣기
    card_nums = list(map(int, input().replace('-', '')))
    
    res = 0
    # 조건 1. 맨 앞자리가 3, 4, 5, 6, 9로 시작
    if card_nums[0] == 3 or card_nums[0] == 4 or card_nums[0] == 5 or card_nums[0] == 6 or card_nums[0] == 9:
        # 조건 2. 카드 번호는 총 16자리
        if len(card_nums) == 16:
            res = 1
    
    print(f'#{test_case} {res}')