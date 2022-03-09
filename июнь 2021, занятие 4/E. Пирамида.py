#

def main(info):
    bd = dict()
    for w_i, h_i in info:
        if w_i not in bd:
            bd[w_i] = h_i
        if h_i > bd[w_i]:
            bd[w_i] = h_i
    res = 0
    for w, h in bd.items():
        res+= bd[w]
    return res
if __name__ == '__main__':
    n = int(input())
    info =[]
    for _ in range(n):
        x = list(map(int, input().split()))
        info.append(x)
    res = main(info)
    print(res)

    assert main([[3, 1], [2, 2], [3, 3]]) == 5