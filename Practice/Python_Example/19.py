# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

number = 123

if number == 0:
    digit = 1

else:
    digit = 0

    while number > 0:
        number //= 10
        digit += 1

print(digit)

# 로그로 풀기
import math
print(int(math.log10(123)) + 1)