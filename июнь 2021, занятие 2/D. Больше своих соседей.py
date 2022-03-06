# Дан список чисел. Определите, сколько в этом списке элементов, которые
# больше двух своих соседей и выведите количество таких элементов.

def find_elements(mass):
    res = 0
    for i in range(1, len(mass) - 1):
        if mass[i - 1] < mass[i] and mass[i] > mass[i + 1]:
            res += 1
    return res


def main():
    mass = list(map(int, input().split()))
    res = find_elements(mass)
    print(res)


if __name__ == "__main__":
    main()

    assert find_elements(mass=[1, 2, 3, 4, 5]) == 0
    assert find_elements(mass=[5, 4, 3, 2, 1]) == 0
    assert find_elements(mass=[1, 5, 1, 5, 1]) == 2
    assert find_elements(mass=[]) == 0
    assert find_elements(mass=[-2,-1,-3]) == 1
    assert find_elements(mass=[-1,0,-3]) == 1