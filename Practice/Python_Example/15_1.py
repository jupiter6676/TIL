# 문자열 word가 주어질 때, 해당 문자열에서 
# a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

def index_(word):
    idx = 0
    for ch in word:
        if ch == 'a':
            print(idx)
            break

        idx += 1
    # break가 실행되지 않으면
    # 즉 'a'가 없으면 else문 실행
    else:
        print(-1)

word1 = 'banana'
word2 = 'apple'
word3 = 'kiwi'

index_(word1)
index_(word2)
index_(word3)