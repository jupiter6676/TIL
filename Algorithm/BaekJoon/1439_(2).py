S = input()
cnt = 0 # 수가 변화한 횟수 (0 → 1 혹은 1 → 0)
prev = '?'

for c in S:
    # 수가 변화했다면
    if c != prev:
        prev = c
        cnt += 1

print(cnt // 2) # 뒤집어야 할 횟수