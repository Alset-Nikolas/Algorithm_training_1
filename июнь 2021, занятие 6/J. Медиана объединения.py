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
    return res


N, K = list(map(int, input().split()))
Lists = []
for i in range(N):
    Lists.append(list(map(int, input().split())))
for i in range(N):
    first_list = Lists[i]
    for j in range(i + 1, N):
        second_list = Lists[j]
        print(calc_item(K, first_list, second_list))
