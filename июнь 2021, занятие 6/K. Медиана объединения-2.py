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
    return res



n, k = list(map(int, input().split()))
data  = []
for i in range(n):
    x1, d1, a, c, m = list(map(int, input().split()))
    d = [d1]
    x = [x1]
    for i in range(1,k):
        d.append((a*d[i-1] + c)%m)
        x.append(x[i-1] + d[i-1])
    data.append(x)

for i in range(n):
    first_list = data[i]
    for j in range(i + 1, n):
        second_list = data[j]
        print(calc_item(k, first_list, second_list))
