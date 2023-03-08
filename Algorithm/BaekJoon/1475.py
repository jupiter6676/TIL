N = input()
dic = dict()

for num in N:
    dic[num] = dic.get(num, 0) + 1

max_v = 0
max_k = 0
for k, v in dic.items():
    if v > max_v:
        max_v = v
        max_k = k
    
    # 만약 6이 2번, 1이 2번이면 max_k = 1이 되도록
    # 왜냐면 20번째 줄 if문에서 걸리면 안 되니깐
    if v == max_v and not (k == '6' or k == '9'):
        max_v = v
        max_k = k

if max_k == '6' or max_k == '9':
    res = max_v - abs(dic.get('6', 0) - dic.get('9', 0)) // 2
else:
    res = max_v

print(res)

'''
66123457801
답: 2
'''