a, b = map(int, input().split())

res = '>' if a > b else ('<' if a < b else '==')
print(res)