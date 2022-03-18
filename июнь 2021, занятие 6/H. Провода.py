def main(k, mass):
    res = 0
    mass.sort()
    left_len = 0
    right_len = mass[-1]
    while right_len > left_len:
        middle_len = (left_len + right_len + 1) // 2
        # print(left_len, middle_len, right_len)
        if sum([x//middle_len for x in mass]) >= k :
            left_len = middle_len
        else:
            right_len = middle_len - 1
    return left_len

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    mass = []
    for i in range(n):
        mass.append(int(input()))
    res = main(k, mass)
    print(res)

    # assert main(11, [802, 743, 457, 539]) == 200
    '''5 11
802 743 457 539'''