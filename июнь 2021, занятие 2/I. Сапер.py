def real_pprint(data):
    for line in data:
        for el in line:
            print(el, end=" ")
        print()


def pprint(mass):
    for line_i in range(1, len(mass) - 1):
        for el_j in range(1, len(mass[0]) - 1):
            print(mass[line_i][el_j], end=" ")
        print()


def new_data(data):
    new_data = [[] for x in range(len(data) - 2)]
    for line_i in range(1, len(data) - 1):
        for el_j in range(1, len(data[0]) - 1):
            new_data[line_i - 1].append(data[line_i][el_j])

    return new_data


def sapper(lines, column, bombs_coords):
    data = [[0 for x in range(column + 2)] for y in range(lines + 2)]
    add_bomb(data=data, bombs_coords=bombs_coords)
    data_res = new_data(data)
    return data_res


def add_bomb(data, bombs_coords):
    for x, y in bombs_coords:
        data[x][y] = "*"
        if data[x - 1][y - 1] != "*":
            data[x - 1][y - 1] += 1
        if data[x][y - 1] != "*":
            data[x][y - 1] += 1
        if data[x - 1][y] != "*":
            data[x - 1][y] += 1
        if data[x + 1][y + 1] != "*":
            data[x + 1][y + 1] += 1
        if data[x][y + 1] != "*":
            data[x][y + 1] += 1
        if data[x + 1][y] != "*":
            data[x + 1][y] += 1
        if data[x - 1][y + 1] != "*":
            data[x - 1][y + 1] += 1
        if data[x + 1][y - 1] != "*":
            data[x + 1][y - 1] += 1


def main():
    lines, column, bomb = list(map(int, input().split()))
    bombs_coords = []
    for i in range(bomb):
        bombs_coords.append(list(map(int, input().split())))
    res = sapper(lines, column, bombs_coords)
    real_pprint(res)


if __name__ == "__main__":
    main()

    assert sapper(3, 2, [[1, 1],
                         [2, 2]]) == [['*', 2],
                                      [2, "*"],
                                      [1, 1]]
    assert sapper(2, 2, []) == [[0, 0],
                                [0, 0]]
    assert sapper(4, 4, [[1, 3],
                         [2, 1],
                         [4, 2],
                         [4, 4]]) == [[1, 2, "*", 1],
                                      ["*", 2, 1, 1],
                                      [2, 2, 2, 1],
                                      [1, "*", 2, "*"]]
