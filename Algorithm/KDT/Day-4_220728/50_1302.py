N = int(input())

book_dict = dict()

for _ in range(N):
    title = input()
    book_dict[title] = book_dict.get(title, 0) + 1

# 판매량 내림차순 정렬 → 책 이름 오름차순 정렬
best_seller = sorted(book_dict.items(), key=lambda x: (-x[1], x[0]))
print(best_seller[0][0])