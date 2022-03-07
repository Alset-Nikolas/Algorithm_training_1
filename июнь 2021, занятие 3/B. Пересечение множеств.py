def main(mass1, mass2):
    return sorted(list(mass1 & mass2))


if __name__ == "__main__":
    mass1 = set(list(map(int, input().split())))
    mass2 = set(list(map(int, input().split())))
    print(*main(mass1, mass2))

    assert main(set([1, 3, 2]), set([4, 3, 2])) == [2, 3]
    assert main(set([1, 2, 6, 4, 5, 7]), set([10, 2, 3, 4, 8])) == [2, 4]
