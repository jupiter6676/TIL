# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

def cntVowels(word):
    cnt = 0

    for ch in word:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            cnt += 1

    print(cnt)

def cntVowels_2(word):
    for ch in word:
        if ch in 'aeiou':
            cnt += 1

word1 = 'apple'
word2 = 'aeiou'
word3 = 'zxcvb'

cntVowels(word1)
cntVowels(word2)
cntVowels(word3)