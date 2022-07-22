def rectangle(w, h):
    area = w * h
    perimeter = (w + h) * 2

    return area, perimeter

a, b = map(int, input().split())

print(rectangle(a, b))