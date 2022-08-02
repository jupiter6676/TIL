import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(T):
    # r: 광고 X 수익
    # e: 광고 O 수익
    # c: 광고 O 비용
    r, e, c = map(int, input().split())

    if r > e - c:
        print('do not advertise')
    elif r < e - c:
        print('advertise')
    else:
        print('does not matter')