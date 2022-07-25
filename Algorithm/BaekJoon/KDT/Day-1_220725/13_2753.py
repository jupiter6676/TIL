# 윤년
year = int(input())

# 1) 4의 배수이면서, 100의 배수가 아님
if year % 4 == 0 and year % 100 != 0:
    print(1)
# 2) 400의 배수
elif year % 400 == 0:
    print(1)
# 3) 윤년 X
else:
    print(0)