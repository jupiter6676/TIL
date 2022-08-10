w = list()
k = list()

for _ in range(10):
    w.append(int(input()))

for _ in range(10):
    k.append(int(input()))

w.sort(reverse=True)
k.sort(reverse=True)

w_total = w[0] + w[1] + w[2]
k_total = k[0] + k[1] + k[2]

print(w_total, k_total)