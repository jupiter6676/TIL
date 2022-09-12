T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    lst_1 = [False] * (N + 1) # 모든 학생의 과제 제출 여부
    lst_2 = list(map(int, input().split()))   # 과제를 제출한 사람

    for i in lst_2:
        lst_1[i] = True

    print(f'#{t}', end=' ')
    for i in range(1, N + 1):
        if not lst_1[i]:
            print(i, end=' ')
    print()

'''
2
5 3
2 5 3
7 2
4 6
'''