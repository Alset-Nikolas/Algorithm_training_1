def main(g, W):
    g_int = len(g)
    w_int = len(W)
    res = 0

    def create_info(text):
        dict_probe = dict()
        for y in text:
            if y not in dict_probe:
                dict_probe[y] = 0
            dict_probe[y] += 1
        return dict_probe

    def compare_dict(dict_base, dict_probe):
        res = 0
        for x in dict_base:
            if x in dict_probe and dict_probe[x] == dict_base[x]:
                res += dict_base[x]
        return res

    def modification_new_el(dict_base, dict_probe, new_el, modif):
        if new_el in dict_base:
            if new_el in dict_probe:
                dict_probe[new_el] += modif
            else:
                if modif == 1:
                    dict_probe[new_el] = 1
                else:
                    dict_probe[new_el] = 0

    dict_base = create_info(g)
    dict_probe = create_info(W[0:g_int])
    if compare_dict(dict_base, dict_probe) == g_int:
        res += 1
    for i in range(g_int, w_int):
        modification_new_el(dict_base, dict_probe, W[i], 1)
        modification_new_el(dict_base, dict_probe, W[i - g_int], -1)
        if compare_dict(dict_base, dict_probe) == g_int:
            res += 1
    return res


if __name__ == '__main__':
    g_int, w_int = list(map(int, input().split()))
    g = input()
    W = input()
    res = main(g, W)
    print(res)

    assert main("cAda", "AbrAcadAbRa") == 2

    # import random
    #
    # test_list = ["A", "B", "C", "D"]
    # while 1:
    #     el1 = "".join([random.choice(test_list) for x in range(5)])
    #     el2 = "".join([random.choice(test_list) for x in range(15)])
    #
    #     if main2(el1, el2) != main(el1, el2):
    #         print(el1, el2, main2(el1, el2), main(el1, el2))
    #         break
