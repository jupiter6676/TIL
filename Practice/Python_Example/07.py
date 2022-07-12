# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

def min_(list):
    MIN = list[0]

    for num in list:
        if num < MIN:
            MIN = num
    
    return MIN

numbers1 = [0, 20, 100]
numbers2 = [0, 20, 100, 50, -60, 50, 100] # -60
numbers3 = [0, 1, 0] # 0
numbers4 = [-10, -100, -30] # -100

print(min_(numbers1))
print(min_(numbers2))
print(min_(numbers3))
print(min_(numbers4))