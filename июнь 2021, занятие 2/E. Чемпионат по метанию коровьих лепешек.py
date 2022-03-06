
def place_vasia(mass):
    res = 0
    if len(mass) < 3 or any(x < 0 for x in mass):
        return 0
    mass_sort = sorted(mass, reverse=True)
    winner_index = mass.index(mass_sort[0])
    vasia_el = None
    for number_shot in range(winner_index + 1, len(mass) - 1):
        el = mass[number_shot]
        if el % 10 == 5:
            if mass[number_shot + 1] < mass[number_shot]:
                    if vasia_el is None or vasia_el < el:
                        vasia_el = el
                        res = mass_sort.index(el) + 1

    return res





def main():
    n = input()
    mass = list(map(int, input().split()))
    res = place_vasia(mass)
    print(res)

    assert place_vasia([10, 20, 15, 10, 30, 5, 1]) == 6
    assert place_vasia([15, 15, 10]) == 1
    assert place_vasia([10, 15, 20]) == 0
    assert place_vasia([10, 10, 15]) == 0
    assert place_vasia([10, 10, 15]) == 0
    assert place_vasia([35, 25, 15]) == 2
    assert place_vasia([35, 35, 15]) == 1
    assert place_vasia([35, 35, 35]) == 0
    assert place_vasia([]) == 0
    assert place_vasia([1, 3, 2]) == 0
    assert place_vasia([15, 5, 2]) == 2
    assert place_vasia([15, 5, 2]) == 2
    assert place_vasia([15, 5, 5, 2]) == 2
    assert place_vasia([15, 15, 5, 2]) == 1
    assert place_vasia([15, 15, 5, 5]) == 1
    assert place_vasia([0, 0, 0, 0]) == 0
    assert place_vasia([0, 0, 5, 0]) == 0
    assert place_vasia([10, 20, 15, 10, 30, 5, 1]) == 6
    assert place_vasia([15, 15, 10]) == 1
    assert place_vasia([10, 15, 20]) == 0
    assert place_vasia([555, 76, 661, 478, 889, 453, 555, 359, 601, 835]) == 5
    assert place_vasia([17, 15, 3, 1, 22]) == 0
    assert place_vasia([17, 15, 3, 1, 22]) == 0



if __name__ == "__main__":
    main()
