def main(r, distances):
    res = 0
    j = 1
    len_dist = len(distances)
    for i in range(len_dist):
        while j < len_dist and distances[j] - distances[i] <= r:
            j += 1
        else:
            res += len_dist-j
    return res


if __name__ == '__main__':
    n, r = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    res = main(r, distances)
    print(res)

    assert main(4, [1, 3, 5, 8]) == 2
    assert main(0, [1, 3, 5, 8, 12]) == 10
    assert main(1, [1, 3, 5, 8, 12]) == 10
    assert main(2, [1, 3, 5, 8, 12]) == 8
    assert main(2, [1, 3]) == 0
    assert main(1, [1, 3]) == 1
    assert main(5, [1, 3, 4, 10]) == 3

