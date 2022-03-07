def main(info):
    road = [None] * len(info)
    real = 0
    for after, before in info:
        if 10000 >= after >= 0 and 10000 >= before >= 0:
            if after + before + 1 == len(road):
                my_index = before
                if 0 <= my_index < len(road) and road[my_index] is None:
                    real += 1
                    road[my_index] = True
    return real


if __name__ == '__main__':
    n = int(input())
    info = []
    for i in range(n):
        info.append(list(map(int, input().split())))
    res = main(info=info)
    print(res)

    assert main([[2, 0], [0, 2], [2, 2]]) == 2
    assert main([[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]) == 5
    assert main([[9, 1], [8, 1], [7, 2], [6, 2], [5, 3], [4, 4], [3, 6], [2, 7], [1, 9], [0, 8]]) == 4

    assert main([[0, 4], [1, 3], [2, 2], [4, 0], [4, 0]]) == 4
    assert main([[0, 4], [1, 3], [4, 0], [4, 0], [4, 0]]) == 3
    assert main([[0, 4], [1, 3], [3, 0], [4, 0], [4, 0]]) == 3
    assert main([[0, 0], [0, 0]]) == 0
    assert main([]) == 0
    assert main([[1, 0], [0, 1]]) == 2
    assert main([[1, 0], [-1, 3]]) == 1
    assert main([[1, 0], [1, 0]]) == 1
    assert main([[1, 1], [2, 0], [0, 1]]) == 2
    assert main([[1, 1], [2, 0], [0, 1]]) == 2
