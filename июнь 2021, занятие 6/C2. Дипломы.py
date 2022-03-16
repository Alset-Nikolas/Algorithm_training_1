def main(w, h, n):
    mass = range(0, (w + h) * n)
    start = 0
    end = len(mass)
    while end > start:
        middle = (start + end) // 2
        if (mass[middle] // w) * (mass[middle] // h) >= n:
            end = middle
        else:
            start = middle + 1

    return mass[start]


if __name__ == '__main__':
    w, h, n = list(map(int, input().split()))
    res = main(w, h, n)
    print(res)

    assert main(2, 3, 10) == 9
