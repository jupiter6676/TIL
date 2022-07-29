import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    cnt = dict()

    # key: 변의 길이, value: 변의 길이가 나온 횟수
    for num in lst:
        cnt[num] = cnt.get(num, 0) + 1
    
    res = 0
    for k, v in cnt.items():
        # 개수가 홀수인 것이 나머지 변의 길이
        if v % 2 != 0:
            res = k
    
    print(f'#{test_case} {res}')