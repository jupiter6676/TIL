# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

def max_(list):
    MAX = list[0]

    for num in list:
        if num > MAX:
            MAX = num
    
    return MAX

numbers1 = [0, 20, 100]
numbers2 = [0, 20, 100, 50, -60, 50, 100] # 100
numbers3 = [0, 1, 0] # 1
numbers4 = [-10, -100, -30] # -10

print(max_(numbers1))
print(max_(numbers2))
print(max_(numbers3))
print(max_(numbers4))