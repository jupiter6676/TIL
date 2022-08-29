# 주어진 리스트 numbers에서 두 번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

def second_(list):
    MAX = list[0]
    SECOND = list[0]

    for num in list:
        if num > MAX:
            SECOND = MAX
            MAX = num
        elif SECOND < num < MAX:
            SECOND = num

    return SECOND

numbers1 = [0, 20, 100, 40]
numbers2 = [0, 20, 100, 50, -60, 50, 100] # 50
numbers3 = [0, 1, 0] # 0
numbers4 = [-10, -100, -30] # -10

print(second_(numbers1))
print(second_(numbers2))
print(second_(numbers3))
print(second_(numbers4))