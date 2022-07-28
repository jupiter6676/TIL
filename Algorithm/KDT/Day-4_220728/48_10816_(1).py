n = int(input())

# 가지고 있는 카드 덱 n개
deck = list(map(int, input().split()))
deck_dict = dict()

for key in deck:
    deck_dict[key] = deck_dict.get(key, 0) + 1


m = int(input())
# 갖고있는 카드들에서, 이 숫자들이 몇 번 나오는지
nums = list(map(int, input().split()))
nums_cnt = [0] * m

for i in range(m):
    if deck_dict.get(nums[i]):
        nums_cnt[i] = deck_dict[nums[i]]

for num in nums_cnt:
    print(num, end=' ')