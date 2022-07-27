def gcd(x, y):
    if x % y == 0:
        return y
    
    # X % Y = R이라 하면,
    # X와 Y의 최대공약수
    # = Y와 R의 최대공약수
    return gcd(y, x % y)

a, b = map(int, input().split())

print(gcd(a, b))
print(a * b // gcd(a, b))