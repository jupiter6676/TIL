dic = dict()
sum_ = 0

for _ in range(10):
    num = input()

    sum_ += int(num)
    dic[num] = dic.get(num, 0) + 1

dic = sorted(dic.items(), key=lambda x: -x[1])

print(sum_ // 10)   # 평균
print(dic[0][0])    # 최빈값