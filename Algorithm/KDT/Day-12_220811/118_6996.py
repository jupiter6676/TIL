N = int(input())

for _ in range(N):
    a_dict = dict()
    b_dict = dict()

    a, b = input().split()

    for ch in a:
        a_dict[ch] = a_dict.get(ch, 0) + 1
    for ch in b:
        b_dict[ch] = b_dict.get(ch, 0) + 1

    if a_dict == b_dict:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')