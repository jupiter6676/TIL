# a, b는 세 자리 자연수
a = int(input())
b = input()

# b의 1의 자리 수부터 * a
for digit in b[::-1]:
    digit = int(digit)
    print(a * digit)

print(a * int(b))