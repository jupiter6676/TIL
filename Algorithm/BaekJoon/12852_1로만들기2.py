import sys
input = sys.stdin.readline

N = int(input())
dp_cnt = [0] * (N + 1)
dp_seq = [[1] for _ in range(N + 1)]

for i in range(1, N + 1):
    if i * 3 <= N:
        if dp_cnt[i * 3]:
            if dp_cnt[i * 3] > dp_cnt[i] + 1:
                dp_cnt[i * 3] = dp_cnt[i] + 1
                dp_seq[i * 3] = [i * 3] + dp_seq[i]

        else:
            dp_cnt[i * 3] = dp_cnt[i] + 1
            dp_seq[i * 3] = [i * 3] + dp_seq[i]

    if i * 2 <= N:
        if dp_cnt[i * 2]:
            if dp_cnt[i * 2] > dp_cnt[i] + 1:
                dp_cnt[i * 2] = dp_cnt[i] + 1
                dp_seq[i * 2] = [i * 2] + dp_seq[i]

        else:
            dp_cnt[i * 2] = dp_cnt[i] + 1
            dp_seq[i * 2] = [i * 2] + dp_seq[i]

    if i + 1 <= N:
        if dp_cnt[i + 1]:
            if dp_cnt[i + 1] > dp_cnt[i] + 1:
                dp_cnt[i + 1] = dp_cnt[i] + 1
                dp_seq[i + 1] = [i + 1] + dp_seq[i]

        else:
            dp_cnt[i + 1] = dp_cnt[i] + 1
            dp_seq[i + 1] = [i + 1] + dp_seq[i]

# print(dp_cnt[1:])
# print(dp_seq[1:])
print(dp_cnt[N])
print(*dp_seq[N])