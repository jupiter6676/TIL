filter = 'CAMBRIDGE'

s = input()
censored = ''

for ch in s:
    if ch in filter:
    # if ch == 'C' or ch == 'A' or ch == 'M' or ch == 'B' or ch == 'R' or ch == 'I' or ch == 'D' or ch == 'G' or ch == 'E':
        continue
    censored += ch

print(censored)