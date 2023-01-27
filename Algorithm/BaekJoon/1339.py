N = int(input())
words = [input() for _ in range(N)]
alpha = dict()    # 알파벳 → 숫자

for word in words:
    for i in range(len(word)):
        alpha[word[i]] = alpha.get(word[i], 0) + 10 ** (len(word) - i - 1)

nums = sorted(alpha.values(), reverse=True)

i = 9
res = 0

for num in nums:
    res += num * i
    i -= 1

print(res)