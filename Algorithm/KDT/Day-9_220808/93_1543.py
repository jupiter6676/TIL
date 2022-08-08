string = input()
word = input()

i = 0
cnt = 0

while i < len(string):
    substring = string[i : i + len(word)]

    if substring == word:
        cnt += 1
        i += len(word)
    else:
        i += 1

print(cnt)

# print(string.count(word))