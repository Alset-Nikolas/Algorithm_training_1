def pprint(res):
    len_res, res_items = res
    print(len_res)
    for x in res_items:
        print(*x)
    # with open("output.txt" , "w") as f:
    #     len_res = str(len_res) + '\n'
    #
    #     f.write(len_res)
    #     for x in res_items:
    #         y = " ".join(str(x) for x in x) + '\n'
    #         f.write(y)


def circle_options(x, y, d):
    vars_cords = set()
    x_min_var = x - d
    x_max_var = x + d
    y_min_var = y - d
    y_max_var = y + d
    for x_i in range(x_min_var, x_max_var + 1, 1):
        for y_j in range(y_min_var, y_max_var + 1, 1):
            if abs(x_i - x) + abs(y_j - y) <= d:
                vars_cords.add((x_i, y_j))

    return vars_cords


def check_t(old_vars, t):
    res = set()

    for x_new, y_new in old_vars:
        x_min_var = x_new - t
        x_max_var = x_new + t
        y_min_var = y_new - t
        y_max_var = y_new + t
        for x_probe in range(x_min_var, x_max_var + 1, 1):
            for y_probe in range(y_min_var, y_max_var + 1, 1):
                if abs(x_new - x_probe) + abs(y_new - y_probe) <= t:
                    res.add((x_probe, y_probe))
    return res


def main(t, d, info):
    old_vars = {(0, 0)}
    for x, y in info:
        old_vars = circle_options(x, y, d) & check_t(old_vars, t)
    return [len(old_vars), old_vars]


if __name__ == '__main__':
    t, d, n = list(map(int, input().split()))
    info = []
    for x in range(n):
        info.append(list(map(int, input().split())))
    res = main(t, d, info)
    pprint(res)
    # res = main(2, 1, [[0, 0]])
    # print(res)
    #
    assert main(2, 1, [[0, 1], [-2, 1], [-2, 3], [0, 3], [2, 5]]) == [2, [(1, 5), (2, 4)]]
    assert main(1, 1, [[0, 0]]) == [5, [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]]
    assert main(1, 10, [[0, 0]]) == [5, [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]]
    assert main(2, 1, [[0, 0]]) == [5, [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]]
