N = int(input())
packs = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)  # dp[i]: 카드 i개 → 최대 금액

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + packs[j])

# print(dp)
print(dp[N])


'''
for i in range(1, N + 1):
    tmp_list = []

    for j in range(1, i + 1):
        if i % j == 0:
            tmp_list.append(packs[j] * (i // j))
        elif i > j:
            tmp_list.append(packs[j] + dp[i - j])

    # print(tmp_list)
    dp[j] = max(tmp_list)

# print(dp)
print(dp[N])
'''

'''
7
742 3302 5186 6619 567 5068 8591
답: 11805

6
1 5 6 1 1 1
답: 15

12
1 1 6 8 11 1 1 1 1 1 1 1
답: 25
'''