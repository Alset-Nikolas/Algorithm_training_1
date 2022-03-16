def main(mass_N, mass_K):
    '''Для каждого из чисел второй последовательности найдите ближайшее к нему в первой.'''
    mass_N = sorted(mass_N)
    ans = [0] * len(mass_K)
    for i, el in enumerate(mass_K):
        start = 0
        end = len(mass_N)
        while end - start != 1:
            middle = (end + start) // 2
            if mass_N[middle] > el:
                end = middle
            else:
                start = middle
        if end == len(mass_N) or abs(mass_N[start] - el) <= abs(mass_N[end] - el):
            ans[i] = mass_N[start]
        else:
            ans[i] = mass_N[end]
    return ans


if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    mass_N = list(map(int, input().split()))
    mass_K = list(map(int, input().split()))

    res = main(mass_N, mass_K)
    for x in res:
        print(x)

    assert main([1, 3, 5, 7, 9, ], [2, 4, 8, 1, 6, ]) == [1, 3, 7, 1, 5]
    assert main([1, 1, 4, 4, 8, 120], [1, 2, 3, 4, 5, 6, 7, 8, 63, 64, 65]) == [1, 1, 4, 4, 4, 4, 8, 8, 8, 8, 120]
