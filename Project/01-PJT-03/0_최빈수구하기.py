import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for _ in range(T):
    test_case = int(input())
    
    scores = list(map(int, input().split()))
    s_dict = dict()

    # 각 점수가 나온 횟수를 딕셔너리에 저장
    # key: 점수, value: 횟수
    for s in scores:
        s_dict[s] = s_dict.get(s, 0) + 1

    # 최빈수 내림차순 → 점수 내림차순
    res = sorted(s_dict.items(), key=lambda x: (-x[1], -x[0]))
    
    print(f'#{test_case} {res[0][0]}')