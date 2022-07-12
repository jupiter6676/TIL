a, b = map(int, input().split())

# NOR : 둘 다 거짓을 경우만 True
res = not(bool(a) or bool(b))
print(res)