a, b = input().split()
a, b = int(a), int(b)

print(a << b)

# 비트 시프트 연산자
# (n << m) : n의 비트 값을 왼쪽으로 m만큼 이동
# 즉 (n * 2^m) 의 결과
# (n >> m) : (n / 2^m) 의 결과