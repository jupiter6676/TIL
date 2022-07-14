# 주어진 문자열 word가 주어질 때, 
# 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

# 1)
word = 'apple'

print(word[::-1])

# 2)
answer = ''

for ch in word:
    answer = ch + answer    # 정답 제일 앞에 char 추가

print(answer)

# 3)
print(''.join(reversed(word)))

# 4) 여기에 익숙해지자
for i in range(len(word)):
    print(word[len(word) - i - 1], end='')