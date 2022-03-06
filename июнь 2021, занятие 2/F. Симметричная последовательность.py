def is_symmetry(mass):
    reverse_mass = mass[::-1]
    for i in range(len(mass)):
        if reverse_mass[:len(mass)-i] == mass[i:]:
            if i == 0 :
                return 0
            res = reverse_mass[len(mass)-i:]
            return [[len(res)], res]
    return 0


def main():
    n = input()
    mass = list(map(int, input().split()))
    res = is_symmetry(mass)
    if res == 0:
        print(0)
    else:
        for pr in res:
            print(*pr)


if __name__ == "__main__":
    main()

    assert is_symmetry([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 0
    assert is_symmetry([1, 2, 1, 2, 2]) == [[3], [1, 2, 1]]
    assert is_symmetry([1, 2, 3, 4, 5]) == [[4], [4, 3, 2, 1]]
    assert is_symmetry([1, 2, 4, 5]) == [[3], [4, 2, 1]]
    assert is_symmetry([]) == 0