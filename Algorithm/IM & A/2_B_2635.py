N1 = int(input())
max_len = 0

for N2 in range(1, N1 + 1):
    tmp_list = list()

    tmp_list.append(N1)
    tmp_list.append(N2)

    i = 2
    while True:
        N3 = tmp_list[i - 2] - tmp_list[i - 1]

        if N3 < 0:  break

        tmp_list.append(N3)
        i += 1

    if len(tmp_list) > max_len:
        max_len = len(tmp_list)
        res_list = list()

        for num in tmp_list:
            res_list.append(num)
        
print(max_len)
print(*res_list)