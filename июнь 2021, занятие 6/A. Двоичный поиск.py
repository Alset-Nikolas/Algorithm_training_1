def main(mass_N, mass_K):
    mass_N = sorted(mass_N)
    ans = [0]*len(mass_K)
    for i, el in enumerate(mass_K):
        start = 0
        end = len(mass_N)
        while end-start !=1:
            middle = (end + start)//2
            if mass_N[middle] > el:
                end = middle
            else:
                start = middle
        if mass_N[start] != el:
            ans[i] = "NO"
        else:
            ans[i] = "YES"
    return ans


if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    mass_N = list(map(int, input().split()))
    mass_K = list(map(int, input().split()))

    res = main(mass_N, mass_K)
    for x in res:
        print(x)

    assert main([1, 61, 126, 217, 2876, 6127, 39162, 98126, 712687, 1000000000],
                [100, 6127, 1, 61, 200, -10000, 1, 217, 10000, 1000000000, ]) == ["NO", "YES", "YES", "YES", "NO", "NO",
                                                                                  "YES", "YES", "NO", "YES"]

