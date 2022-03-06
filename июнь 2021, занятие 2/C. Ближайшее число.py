def main(mass, find_x):
    if len(mass) == 0:
        return None

    min_distanse, res = abs(mass[0] - find_x), mass[0]
    for el in mass:
        distanse = abs(el - find_x)
        if min_distanse > distanse:
            min_distanse, res = abs(el - find_x), el
    return res


if __name__ == "__main__":
    N = input()
    mass = list(map(int, input().split()))
    find_x = int(input())
    res = main(mass, find_x)
    print(res)

    assert main(mass=[1, 2, 3, 4, 5], find_x=6) == 5
    assert main(mass=[1, 2, 6, 4, 5], find_x=6) == 6
    assert main(mass=[1, 2, 6, 4, 5], find_x=0) == 1
    assert main(mass=[1, 1, 0, -1, 5], find_x=0) == 0
    assert main(mass=[1, 1, 0, -1, 5], find_x=1) == 1
    assert main(mass=[1, 1, 0, -1, 5], find_x=-1) == -1
