x, y = input().split()

sum_ = str(int(x[::-1]) + int(y[::-1]))
rev_sum = int(sum_[::-1])

print(rev_sum)