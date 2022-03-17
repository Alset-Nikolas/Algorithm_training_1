def main(a, b, c):
    "a -> 2, b -> 3, c ->4"
    param = a * 2 + b * 3 + c * 4
    all_q = a + b + c
    min_five = 0
    max_five = all_q
    if max_five == min_five:
        return 1
    while max_five > min_five:
        middle = (max_five + min_five) // 2
        if (param + middle * 5) >= 3.5 * (all_q + middle):
            max_five = middle
        else:
            min_five = middle + 1
    return min_five


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    res = main(a, b, c)
    print(res)

    assert main(2, 0, 0) == 2
    assert main(2, 1, 0) == 3
    assert main(0, 0, 1) == 0
    assert main(0, 1, 0) == 1
