def max_trio(mass):
    if len(mass) == 3:
        return sorted(mass)
    res_positive = []
    res_negative = []
    res_negative_small = []
    for el in mass:
        if el >= 0:
            res_positive.append(el)
            res_positive.sort(reverse=True)
            res_positive = res_positive[:3]
        elif el < 0:
            res_negative.append(el)
            res_negative.sort(reverse=False)
            res_negative = res_negative[:3]
            res_negative_small.append(el)
            res_negative_small.sort(reverse=True)
            res_negative_small = res_negative_small[:3]

    if len(res_negative) > 1:
        if len(res_positive) == 0:
            return sorted(res_negative_small)
        if len(res_positive) == 3:
            if res_negative[0] * res_negative[1] > res_positive[1] * res_positive[2]:
                return sorted([res_negative[0], res_negative[1], res_positive[0]])
            return sorted([res_positive[0], res_positive[1], res_positive[2]])
        return sorted([res_positive[0]] + res_negative[:2])

    if len(res_positive) + len(res_negative) == 3 and len(res_positive) != 0:
        return sorted(res_positive + res_negative)
    if len(res_positive) == 1 and len(res_negative) > 1:
        return sorted([res_positive[0]] + res_negative[:2])

    return sorted(res_positive)


def main():
    mass = list(map(int, input().split()))
    res = max_trio(mass=mass)
    print(*res)


if __name__ == "__main__":
    main()

    assert max_trio([3, 5, 1, 7, 9, 0, 9, -3, 10]) == [9, 9, 10]
    assert max_trio([-5, -30000, -12]) == [-30000, -12, -5]
    assert max_trio([1, 2, 3]) == [1, 2, 3]
    assert max_trio([1, 1, 1, -3, -2, -1]) == [-3, -2, 1]
    assert max_trio([10, 10, 10, -3, -2, -1]) == [10, 10, 10]
    assert max_trio([10, 10, 10, -3, -2, -1, -3000]) == [-3000, -3, 10]
    assert max_trio([0, 10, -3]) == [-3, 0, 10]
    assert max_trio([10, 100, -100, -10]) == [-100, -10, 100]
    assert max_trio([120, 100, -100, -10, 1000]) == [100, 120, 1000]
    assert max_trio([120, 100, 10, 1, 3]) == [10, 100, 120]
    assert max_trio([-120, -100, -10, -1, -3]) == [-10, -3, -1]
    assert max_trio([-120, -100, 10, -1, -3]) == [-120, -100, 10]
    assert max_trio([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-10, -9, 10]
    assert max_trio([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-10, -9, 10]
    assert max_trio([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [10, 11, 12]
    assert max_trio([10, 11, 12, -10, -11, -12]) == [-12, -11, 12]
    assert max_trio([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,-10, -11, -12]) == [11, 12, 13]
    assert max_trio([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, -10, -11, -12]) == [11, 12, 13]
    assert max_trio([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -10, -11, -12]) == [-3, -2, -1]
    assert max_trio([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -10, -11, 12]) == [-13, -12, 12]
    assert max_trio([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -10, 11, 12]) == [-13, -12, 12]
    assert max_trio([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, 10, 11, 12]) == [-13, -12, 12]
    assert max_trio([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, 10, 11, 12]) == [-13, -12, 12]
    assert max_trio([-3, 0, -5, -7]) == [-7, -5, 0]
    assert max_trio([1,2,3]) == [1, 2, 3]
    assert max_trio([1, 0, 3]) == [0, 1, 3]
    assert max_trio([-10, 0, -20, -30, -40]) == [-40, -30, 0]
    #
    # import random
    # while 1:
    #     x = [random.randint(-100, 100) for x in range(random.randint(3,10))]
    #     x[0] = 0
    #     r = max_trio(x)
    #     print(x, max_trio(x))
    #     if len(r) != 3:
    #         exit()


