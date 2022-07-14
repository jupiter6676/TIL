# 문자열 word가 주어질 때, 
# 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

def index_all(word):
    idx = 0
    for ch in word:
        if ch == 'a':
            # 혹은 새 리스트 생성 후 .append(idx)
            print(idx, end=' ')

        idx += 1

    print()

word1 = 'HappyHacking'
word2 = 'banana'
word3 = 'kiwi'

index_all(word1)
index_all(word2)
index_all(word3)