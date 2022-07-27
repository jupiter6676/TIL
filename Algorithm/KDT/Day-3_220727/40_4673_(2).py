'''천재 코드'''

# 1부터 10000까지 숫자들의 전체 집합 U
U = set(range(1, 10001))

# 생성자를 가지는 숫자들(분해합)의 집합
subset = set()

for i in range(1, 10001):
    # i의 각 자릿수 j
    for j in str(i):
        # i에 각 자릿수들의 합을 더함
        # 다 더해지면, i는 분해합이 됨.
        i += int(j)

    subset.add(i)   # 분해합 i를 subset에 추가

# self-number들의 집합 subset_2
# self-number들의 집합 = 전체 집합 - 생성자를 가지는 숫자들의 집합
# 작은 수부터 출력할 수 있도록, 원소들을 정렬
subset_2 = sorted(U - subset)

for num in subset_2:
    print(num)