# 1부터 n까지의 합을 구하여 출력하는 코드를 
# 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

n = 10

# 1)
i = 0
sum = 0

while i <= 10:
    sum += i
    i += 1
print(sum)

# 2)
sum = 0

for i in range(n + 1):
    sum += i
print(sum)