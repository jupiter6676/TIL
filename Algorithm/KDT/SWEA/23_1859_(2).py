'''천재 코드'''

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    # list의 마지막 값을 최대값으로 설정
    max_price = price[-1]
    # 이익 변수 초기화
    profit = 0

    # N-2번째 인덱스부터 0번째 인덱스까지 1씩 감소하면서 반복 순회
    for i in range(N - 2, -1, -1):
        # 만약 현재 매매가가 최대값보다 크면 최대값을 변경
        if price[i] >= max_price:
            max_price = price[i]
        # 현재 매매가가 최대값보다 크지 않으면 차익을 profit 변수에 더해준다
        else:
            profit += max_price - price[i]
    
    # 결과 출력
    print(f'#{test_case} {profit}')