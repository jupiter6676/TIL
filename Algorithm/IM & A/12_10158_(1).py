'''시간 초과 1'''
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

NE = 1  # 오른쪽 위 45도 방향
SW = 0  # 왼쪽 아래 45도 방향

dir_ = NE

while True:
    if t == 0:  break

    if dir_ == NE:
        p += 1
        q += 1

        if not (0 < p < w and 0 < q < h):
            dir_ = SW

            if not (p == w and q == h):
                p -= 1
                q += 1

                t -= 1

    else:
        p -= 1
        q -= 1

        if not (0 < p < w and 0 < q < h):
            dir_ = NE

            if not (p == 0 and q == 0):
                p -= 1
                q += 1

                t -= 1

    t -= 1

print(p, q)