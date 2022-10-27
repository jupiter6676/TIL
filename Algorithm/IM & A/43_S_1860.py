import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split()) # 손님 N명, M초에 K개의 붕어빵
    customers = list(map(int, input().split())) # 손님 도착 시각

    is_possible = True
    max_sec = max(customers) # 가장 늦게 입장했을 때의 시간

    ch = [0] * (max_sec + 1)   # 몇 초에 손님이 도착했는지 체크
    for i in range(N):
        ch[customers[i]] = 1

    bread = 0
    for sec in range(max_sec + 1):
        # M초가 지나면 K개의 붕어빵 굽기
        if sec > 0 and sec % M == 0:
            bread += K

        # 손님이 도착했을 때
        if ch[sec]:
            # 붕어빵이 없으면 Impossible
            if bread <= 0:
                is_possible = False
            # 붕어빵이 있으면 하나 판매
            else:
                bread -= 1

    print(f'#{t}', end=' ')
    print('Possible' if is_possible else 'Impossible')


'''
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2
'''

'''
1
46 66 6
10029 4659 3269 6238 277 6404 1754 1788 5109 2386 1814 10710 6247 10117 1149 4097 9301 6215 10399 1736 4805 2140 9517 3995 5596 6407 8259 3680 6476 1351 7811 5533 3863 1876 8345 10823 9466 8695 1553 1452 7425 2080 9585 1948 1213 4517
'''