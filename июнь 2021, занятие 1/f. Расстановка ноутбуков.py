
a1, b1, a2, b2 = map(int, input().split())
w1, h1 = max(a1, b1), min(a1, b1)
w2, h2 = max(a2, b2), min(a2, b2)

if w1 < w2 or w1 < h2:
    w1, w2 = w2, w1
    h1, h2 = h2, h1

size1 = [w1, h1 + h2]
size2 = [w1 + w2, max(h1, h2)]
size3 = [w1 + h2, max(w2, h1)]
size4 = [w1, h1 + w1]

all_size = [size1, size2, size3, size4]

min_s = all_size[0][0] * all_size[0][1]
for size in all_size:
    x, y = size
    if x * y < min_s:
        min_s = x * y

for size in all_size:
    x, y = size
    if x * y == min_s:
        print(x, y)
        # print(y, x)
        break
