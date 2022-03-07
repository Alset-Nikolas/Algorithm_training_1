def main(info):
    high = dict()
    for x, y in info:
        if x not in high:
            high[x] = y
        else:
            high[x] = max(high[x], y)
    return len(high)


if __name__ == '__main__':
    n = int(input())
    info = []
    for _ in range(n):
        info.append(list(map(int, input().split())))
    res = main(info=info)
    print(res)

    assert main([[1, 1], [2, 2], [3, 3], [2, 1], [3, 2], [3, 1]]) == 3
    assert main([[1, 1], [2, 2], [3, 3], [2, 1], [3, 2], [3, 4]]) == 3
