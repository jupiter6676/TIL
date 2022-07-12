a, b = map(int, input().split())

# XNOR → not(XOR) : 두 값이 서로 같을 때 True
res = not(bool(a) ^ bool(b))
print(res)