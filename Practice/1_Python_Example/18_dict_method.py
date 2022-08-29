# 문자열 word가 주어질 때, Dictionary를 활용해서 
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

dic = dict()
word = 'banana'

# 1.
# 딕셔너리에 키-값 추가 (값은 0으로)
for ch in word:
    dic[ch] = 0

# 카운트
for ch in word:
    dic[ch] += 1

# 출력
for k, v in dic.items():
    print(k, v)


# 2.
for ch in word:
    if not ch in dic:   # 딕셔너리에 키가 없으면
        dic[ch] = 0     # 딕셔너리[key] = 0으로 초기화
    else:
        dic[ch] += 1

# 3. get 사용
for ch in word:
    # dic['a'] 없으면 KeyError
    # dic.get('a') 기본값이 None
    # dic.get('a', 0) 기본값이 0
    # → key가 없으면 0으로 만들고, 있으면 value를 가져와서 1 더하는 코드
    dic[ch] = dic.get(ch, 0) + 1