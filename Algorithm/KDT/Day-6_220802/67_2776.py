T = int(input())
for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))

    dict1 = dict()
    for num in note1:
        dict1[num] = dict1.get(num, 0) + 1

    M = int(input())
    note2 = list(map(int, input().split()))

    for num in note2:
        print(1 if dict1.get(num) else 0)