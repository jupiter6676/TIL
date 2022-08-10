a = int(input())
b = int(input())
c = int(input())

# 세 각이 모두 60
if a == 60 and b == 60 and c == 60:
    print('Equilateral')

# 세 각이 모두 60이 아니고, 세 각의 합 180
elif a + b + c == 180:
    # 두 각이 같은 경우
    if a == b or b == c or c == a:
        print('Isosceles')
    # 두 각이 다른 경우
    else:
        print('Scalene')

else:
    print('Error')