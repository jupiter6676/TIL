a, b = map(int, input().split())

# XOR → ^ : 두 값이 서로 다를 경우 True
res = bool(a) ^ bool(b)
print(res)

'''
a = bool(int(a))
b = bool(int(b))

res = (a and (not b)) or ((not a) and b)
print(res)
'''