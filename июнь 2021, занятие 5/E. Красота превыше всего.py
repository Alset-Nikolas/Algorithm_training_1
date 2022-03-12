import math


def main(k, colors):
    left = 0
    all_k = dict()
    len_min = math.inf
    ans = []

    for right in range(len(colors)):
        if colors[right] not in all_k:
            all_k[colors[right]] = 0
        all_k[colors[right]] += 1

        if len(all_k) == k:
            while all_k[colors[left]] > 1:
                all_k[colors[left]] -= 1
                left += 1
            if len_min > abs(left - right):
                len_min = abs(left - right)
                ans = [left + 1, right + 1]

    return ans


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    colors = list(map(int, input().split()))
    res = main(k, colors)
    print(*res)

    assert main(3, [1, 2, 1, 3, 2]) == [2, 4]
    assert main(4, [2, 4, 2, 3, 3, 1]) == [2, 6]
