# n은 원반 개수 (만약 1 2 3의 3개라면)
# 목표: start(A) → end(C)로 원판을 이동해야 한다. (3 → 2 → 1 순으로 도착)

# work(B)는 중간에 원판을 두는 곳 (ex. 3을 end에 두기 위해, 1과 2를 work에 두어야 한다.)
# work에 있던 원반 1과 2를, start를 이용해 end에 옮긴다.
def hanoi(n, start, work, end):
    if n == 1:
        print(start, end)

    else:
        # 1. A에 있던 1 ~ n - 1 원판을, C를 이용하여 B로 옮긴다.
        hanoi(n - 1, start, end, work)

        # 2. A에 있던 n 원판 한 개를, C로 옮긴다.
        print(start, end)

        # 3. B에 있던 1 ~ n - 1 원판을, A를 이용하여 C로 옮긴다.
        hanoi(n - 1, work, start, end)


N = int(input())

print(2 ** N - 1)

if N <= 20:
    hanoi(N, 1, 2, 3)
