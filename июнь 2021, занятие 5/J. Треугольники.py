def main(cords):
    res = 0
    for (x_center, y_center) in cords:
        L_coords = [None] * len(cords)
        L_count = dict()
        for i, (x_other, y_other) in enumerate(cords):
            if x_other != x_center or y_other != y_center:
                L_coords[i] = (x_center - x_other) ** 2 + (y_center - y_other) ** 2

                if L_coords[i] not in L_count:
                    L_count[L_coords[i]] = []
                L_count[L_coords[i]].append(cords[i])

        # print(L_count)
        for L_i, cords_i in L_count.items():
            if len(cords) < 2:
                continue
            add_res = 0
            for first_x, first_y in cords_i:
                for second_x, second_y in cords_i:
                    if first_x != second_x or first_y != second_y:
                        if (first_x - second_x) ** 2 + (first_y - second_y) ** 2 < 4 * L_i:
                            add_res += 1
            res += add_res // 2

    return res


if __name__ == '__main__':
    n = int(input())
    coords = []
    for i in range(n):
        coords.append(tuple(map(int, input().split())))
    res = main(coords)
    print(res)
