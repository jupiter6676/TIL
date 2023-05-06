import sys
input = sys.stdin.readline

roman = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000,
    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
}

num1 = input().rstrip()    # DLIII = 553
num2 = input().rstrip()    # MCMXL = 1000 + 900 + 40 = 1940     2493

sum_ = 0
N = len(num1)
i = 0
while True:
    if i >= N:
        break

    if i < N - 1:
        if roman[num1[i]] >= roman[num1[i + 1]]:
            sum_ += roman[num1[i]]
        else:
            sum_ += roman[num1[i : i + 2]]
            i += 1
    else:
        sum_ += roman[num1[i]]

    i += 1

M = len(num2)
i = 0
while True:
    if i >= M:
        break

    if i < M - 1:
        if roman[num2[i]] >= roman[num2[i + 1]]:
            sum_ += roman[num2[i]]
        else:
            sum_ += roman[num2[i : i + 2]]
            i += 1
    else:
        sum_ += roman[num2[i]]

    i += 1

roman_sorted = sorted(roman.items(), key=lambda x: -x[1])

res = ''
for k, v in roman_sorted:
    if sum_ >= v:
        for _ in range(sum_ // v):
            res += k
            sum_ -= v

print(sum_)
print(res)