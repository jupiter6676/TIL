width, height = map(int, input().split())
N = int(input())

cut_w = [0, height]  # 가로로 몇 번을 자르는지 저장 (행 번호 → height라 생각)
cut_h = [0, width]  # 세로로 몇 번을 자르는지 저장

for _ in range(N):
    s, num = map(int, input().split())

    if s == 0:
        cut_w.append(num)
    else:
        cut_h.append(num)

cut_w.sort()
cut_h.sort()

lst = list()

for i in range(1, len(cut_w)):
    for j in range(1, len(cut_h)):
        tmp = (cut_w[i] - cut_w[i - 1]) * (cut_h[j] - cut_h[j - 1])
        lst.append(tmp)

print(max(lst))