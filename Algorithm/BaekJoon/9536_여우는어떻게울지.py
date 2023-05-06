import sys
input = sys.stdin.readline

for _ in range(int(input())):
    lst = list(input().split()) # 모든 동물의 울음소리
    dic = dict()    # 여우 제외 울음소리

    while True:
        string = input().rstrip()
        
        if string == 'what does the fox say?':
            break

        animal = list(string.split())
        dic[animal[0]] = animal[2]

    new_lst = list()
    for i in range(len(lst)):
        flag = True # 여우 울음소리 = dic의 모든 value와 다른 값을 가짐

        for v in dic.values():
            if v == lst[i]:
                flag = False    # 같은 값이 나오는 순간 False

        if flag:
            new_lst.append(lst[i])

    print(*new_lst)