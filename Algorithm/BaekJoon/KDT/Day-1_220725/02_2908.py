a, b = input().split()

# 뒤집기
a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)