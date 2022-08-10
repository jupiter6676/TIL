a, b = map(int, input().split())

a -= 1
b -= 1

a_row = a % 4
a_col = a // 4

b_row = b % 4
b_col = b // 4

res = abs(b_row - a_row) + abs(b_col - a_col)
print(res)