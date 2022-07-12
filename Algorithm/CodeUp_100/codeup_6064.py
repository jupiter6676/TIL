a, b, c = map(int, input().split())

# 삼항 연산
res = (c if b > c else b) if a > b else (c if a > c else a)
print(res)

'''
if a > b:
    if b > c:
        c
    else:
        b
else:
    if a > c:
        c
    else:
        a
'''