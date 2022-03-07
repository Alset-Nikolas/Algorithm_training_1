def main(mass):
    res = len(set(mass))
    return res


if __name__ == "__main__":
    mass = list(map(int, input().split()))
    res = main(mass)
    print(res)

    assert main([1, 2, 3, 2, 1]) == 3
    assert main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert main([1, 2, 3, 4, 5, 1, 2, 1, 2, 7, 3]) == 6
