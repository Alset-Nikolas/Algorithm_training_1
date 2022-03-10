def main(g_int, w_int, g, W):
    res = 0

    def modification_new_el(dict_probe, new_el, modif):
        if new_el in dict_probe:
            dict_probe[new_el] += modif
            if dict_probe[new_el] < 0:
                dict_probe[new_el] = 0

    dict_base = dict()
    for y in g:
        if y not in dict_base:
            dict_base[y] = 0
        dict_base[y] += 1

    dict_probe = dict()
    for key in dict_base.keys():
        dict_probe[key] = 0
    for i_start in range(g_int):
        modification_new_el(dict_probe, W[i_start], 1)
    if dict_base == dict_probe:
        res += 1
    for i in range(g_int, w_int):
        modification_new_el(dict_probe, W[i], 1)
        modification_new_el(dict_probe, W[i - g_int], -1)
        if dict_base == dict_probe:
            res += 1
    return res


if __name__ == '__main__':
    g_int, w_int = list(map(int, input().split()))
    g = input()
    W = input()
    res = main(g_int, w_int, g, W)
    print(res)
    assert main(4, 11, "cAda", "AbrAcadAbRa") == 2
    assert main(4, 4, "cAda", "cAda") == 1
