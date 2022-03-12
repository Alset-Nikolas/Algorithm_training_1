def main(k, colors):
    left = 0
    all_k = [1] + [0] * k
    len_min = len(colors)
    ans = []
    for right in range(len(colors)):
        all_k[colors[right]] += 1
        while all([x > 0 for x in all_k]):
            if len_min > abs(left - right):
                len_min = abs(left - right)
                ans = [left + 1, right + 1]
            all_k[colors[left]] -= 1
            left += 1
    return ans


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    colors = list(map(int, input().split()))

    res = main(k, colors)
    print(*res)

    assert main(3, [1, 2, 1, 3, 2]) == [2, 4]
    assert main(4, [2, 4, 2, 3, 3, 1]) == [2, 6]
