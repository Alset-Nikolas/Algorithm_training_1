def prefix_func(text, n):
    PI = [0] * len(text)
    for i in range(1, len(text)):
        p = PI[i - 1]
        while p > 0 and text[i] != text[p]:
            if p - 1 < 0:
                p = 0
            else:
                p = PI[p - 1]
        if text[i] == text[p]:
            p += 1
        PI[i] = p
    return PI.cpunt(n)


def main(g, W):
    import itertools
    vars_g = set(itertools.permutations(g))
    res = 0
    for i, x in enumerate(vars_g):
        res += prefix_func("".join(x) + "#" + W, len(g))
    return res



if __name__ == '__main__':
    g_int, w_int = list(map(int, input().split()))
    g = input()
    W = input()
    res = main(g, W)
    print(res)

    assert main("cAda", "AbrAcadAbRa") == 2
    assert main("ab", "abbaabba") == 4
