def main(g, W):
    def create_info(text):
        dict_probe = dict()
        for y in text:
            if y not in dict_probe:
                dict_probe[y] = 0

            dict_probe[y] += 1
        return dict_probe

    dict_base = dict()
    for x in g:
        if x not in dict_base:
            dict_base[x] = 0
        dict_base[x] += 1
    res = 0

    for i in range(w_int):

        if create_info(W[i:g_int + i]) == dict_base:
            res += 1
    return res




if __name__ == '__main__':
    g_int, w_int = list(map(int, input().split()))
    g = input()
    W = input()
    res = main(g, W)
    print(res)

    assert main("cAda", "AbrAcadAbRa") == 2
