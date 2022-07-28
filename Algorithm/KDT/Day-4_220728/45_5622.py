s = input()

dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0
for a in s:
    for i in range(len(dials)):
        if a in dials[i]:
            time += i + 3

print(time)