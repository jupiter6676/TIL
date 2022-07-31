N = int(input())    # N은 항상 홀수
lst = list(map(int, input().split()))

lst.sort()

# N이 홀수 → 중간값은 N / 2 + 1번째
# → 인덱스는 N / 2
print(lst[N // 2])