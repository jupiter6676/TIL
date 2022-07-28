a, b = map(int, input().split())

i = 1
seq = list()

while len(seq) < b:
    # 만약 i가 2라면, 
    # 수열에 [2]를 2번 붙이기
    seq += [i] * i
    
    i += 1

# index: 0부터니까
# [a, b] → [a-1, b-1] → seq[a-1 : b]
sum_ = 0
for i in range(a - 1, b):
    sum_ += seq[i]

print(sum_)