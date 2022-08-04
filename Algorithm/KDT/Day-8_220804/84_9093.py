T = int(input())

for t in range(T):
    s = list(input().split())

    for substring in s:
        rev = substring[::-1]
        print(rev, end=' ')

    print()