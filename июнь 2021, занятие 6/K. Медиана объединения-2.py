'''Топорный вариант'''

def calc_item(k, L, R):
    i_L = 0
    i_R = 0
    res_i = 0
    res = None
    while res_i != k:
        if i_L < len(L) and i_R < len(R):
            if L[i_L] > R[i_R]:
                res = R[i_R]
                i_R += 1
            else:
                res = L[i_L]
                i_L += 1
        elif i_L == len(L):
            res = R[i_R]
            i_R += 1
        elif i_R == len(R):
            res = L[i_L]
            i_L += 1
        res_i += 1
    del i_L, i_R, res_i
    return res


n, k = list(map(int, input().split()))
data = [[] for x in range(n)]
for i in range(n):
    x1, d1, a, c, m = list(map(int, input().split()))
    d = [d1] * k
    x = [x1] * k
    for j in range(1, k):
        d[j] = (a * d[j - 1] + c) % m
        x[j] = x[j - 1] + d[j - 1]
    data[i] = x

    del x, x1, d, d1, a, c, m

for i in range(n):
    for j in range(i + 1, n):
        print(calc_item(k, data[i], data[j]))
    data[i] = []
