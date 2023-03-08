N = int(input())
times = list(map(int, input().split()))

times.sort()

cumulated_sum = 0
for i in range(N):
    cumulated_sum += sum(times[:i + 1])

print(cumulated_sum)