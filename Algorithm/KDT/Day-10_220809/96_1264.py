while True:
    string = input()

    if string == '#':
        break

    cnt = 0
    for ch in string:
        if ch in 'aeiouAEIOU':
            cnt += 1

    print(cnt)