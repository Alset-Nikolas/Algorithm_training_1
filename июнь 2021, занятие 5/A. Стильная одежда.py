from cmath import inf


def main(t_shirts, trousers):
    d_min = inf
    ans = []
    j = 0
    for x in t_shirts:
        x_d_min = abs(x - trousers[j])
        ans_x = [x, trousers[j]]
        while j + 1 < len(trousers) and abs(x - trousers[j + 1]) <= x_d_min:
            x_d_min = abs(x - trousers[j + 1])
            j+=1
            ans_x = [x, trousers[j]]
        # print(x_d_min, d_min)
        if x_d_min < d_min:
            d_min = x_d_min
            ans = ans_x

    return ans


if __name__ == '__main__':
    N = int(input())
    t_shirts = list(map(int, input().split()))
    M = int(input())
    trousers = list(map(int, input().split()))
    res = main(t_shirts, trousers)
    print(*res)

    assert main([3, 4], [1, 2, 3]) == [3, 3]
    assert main([4, 5], [1, 2, 3]) == [4, 3]
    assert main([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 1]
    assert main([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]) == [5, 5]
    assert main([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]) == [5, 5]
    assert main([1, 2, 3, 4, 7, 8, 9], [5]) == [4, 5]
    assert main([5], [5]) == [5, 5]
    assert main([0, 10], [0, 10]) == [0, 0]
    assert main([0, 10], [11, 12]) == [10, 11]
    assert main([0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9, 10]) == [10, 10]
    assert main([0, 2, 4, 6, 8], [1, 3, 5, 7, 9]) == [0, 1]
    assert main([0, 2, 4, 6, 8], [1]) == [0, 1]
