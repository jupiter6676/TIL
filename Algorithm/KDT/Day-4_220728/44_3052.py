r_dict = dict()
for _ in range(10):
    n = int(input())
    r = n % 42

    r_dict[r] = r_dict.get(r, 0) + 1

# .keys() → O(1)
# len() → O(1)
print(len(r_dict.keys()))