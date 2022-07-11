f1, f2 = input().split()

f1 = float(f1)
f2 = float(f2)
div = f1 / f2

# round(div, 3) 하니까
# 10.0 0.0001 했을 때 100000.000이 아니라
# 100000.0 뜬다고 틀림
print(format(div, ".3f"))