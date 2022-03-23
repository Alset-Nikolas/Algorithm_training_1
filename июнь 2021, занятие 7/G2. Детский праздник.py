def calc_optimal_T(mans):
    def check(t_mid):
        total_count = 0
        for t_one, z, t_man in mans:
            count_times_with_rest, t_rem = divmod(t_mid, t_man)
            count_without_rest = min(t_rem // t_one, z)
            total_count += count_times_with_rest * z + count_without_rest
        return total_count >= m

    l = -1
    r = TIME_MAX + 1
    while r - l > 1:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    return r


if __name__ == '__main__':
    m, n = map(int, input().split())
    mans = [None] * n
    for i in range(n):
        t_one, z, y = map(int, input().split())
        mans[i] = (t_one, z, t_one * z + y)

    TIME_MAX = 200 * 15000

    t_ans = calc_optimal_T(mans)
    rem_count = m
    ans_list = [None] * n
    for i, (t_one, z, t_man) in enumerate(mans):
        count_times_with_rest, t_rem = divmod(t_ans, t_man)
        count_without_rest = min(t_rem // t_one, z)
        count_man = count_times_with_rest * z + count_without_rest
        ans_list[i] = rem_count if count_man > rem_count else count_man
        rem_count -= count_man
        if rem_count < 0:
            rem_count = 0

    print(t_ans)
    print(*ans_list)
