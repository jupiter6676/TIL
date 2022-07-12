n = int(input())

i = 1
total = 0

# total == n인 경우, i의 값이 2번 증가함
while total < n:    
    total += i
    i += 1

i -= 1

print(i)