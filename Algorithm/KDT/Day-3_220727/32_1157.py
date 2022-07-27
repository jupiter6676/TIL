s = input()

alphabet_cnt = dict()   # 대문자만 저장

for ch in s:
    # 알파벳을 모두 대문자로
    CH = ch.upper()
    
    alphabet_cnt[CH] = alphabet_cnt.get(CH, 0) + 1

max_cnt = -9999999  # 0으로 하니까 안 되네..
max_letters = list()

for item in alphabet_cnt.items():
    if item[1] > max_cnt:
        max_cnt = item[1]   # 등장 횟수
        res = item[0]       # 알파벳
    elif item[1] == max_cnt:
        res = '?'

print(res)