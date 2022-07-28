n = int(input())

# 가지고 있는 카드 덱 n개
deck = list(map(int, input().split()))
deck_dict = dict()

for key in deck:
    deck_dict[key] = deck_dict.get(key, 0) + 1

m = int(input())
# 갖고있는 카드들에서, 이 숫자들이 몇 번 나오는지
nums = list(map(int, input().split()))

for num in nums:
    # num으로 된 key가 있으면 대응되는 value를,
    # key가 없으면 0을 출력
    print(deck_dict.get(num, 0), end=' ')