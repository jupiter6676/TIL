def recur(s, left, right):
    global depth

    depth += 1

    if left >= right:
        return 1    # True
    
    elif s[left] != s[right]:
        return 0    # False

    else:
        return recur(s, left + 1, right - 1)


T = int(input())
for _ in range(T):
    S = input()
    depth = 0

    print(recur(S, 0, len(S) - 1), depth)