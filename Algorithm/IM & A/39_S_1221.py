import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(1, T + 1):
    tc, N = input().split()    # '#tc N'
    N = int(N)
    nums_list = list(input().split())

    nums_dict = {
        'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
        'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9,
    }

    new_nums_list = list()

    for i in range(N):
        # [0, 'ZRO']과 같은 형태로 저장
        new_nums_list.append([nums_dict[nums_list[i]], nums_list[i]])

    new_nums_list = sorted(new_nums_list, key=lambda x: x[0])

    print(tc)
    for i in range(N):
        print(new_nums_list[i][1], end=' ')
    print()