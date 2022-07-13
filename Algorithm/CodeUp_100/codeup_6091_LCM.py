'''
def isCoprime(n, m):    # n, m은 2 이상의 자연수
    i = 2   # 공약수인가?
    if n <= m:
        while i <= n:
            if n % i == 0 and m % i == 0:
                return False
            i += 1
        return True

    else:
        while i <= m:
            if n % i == 0 and m % i == 0:
                return False
            i += 1
        return True
'''

a, b, c = map(int, input().split())

i = 2
while True:
    if i % a == 0 and i % b == 0 and i % c == 0:
        break
    i += 1

print(i)