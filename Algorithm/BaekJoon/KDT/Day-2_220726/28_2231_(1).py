N = int(input())

res = 0
c = 1   # 생성자(constructor)
while c < N:
    d = c   # 분해합(decompose) 초기화 = c

    # c의 자릿수를 분해합에 더해줌 (map 쓰면 되는데...)
    for digit in str(c):
        d += int(digit)

    # 분해합이 초기 input과 같으면
    if d == N:
        res = c # 생성자로 res 갱신 (생성자 없으면 갱신 X)
        break

    c += 1

print(res)