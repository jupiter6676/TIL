# 주어진 문자열 word가 주어질 때, 
# 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

word = 'apple'

# 1)
word2 = word.replace('a', '')
print(word2)

# 2)
result = ''
for ch in word:
    if ch != 'a':
        result = result + ch

print(result)