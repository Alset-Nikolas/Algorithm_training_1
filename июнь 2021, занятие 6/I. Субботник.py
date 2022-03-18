def calc_group(delta, porog, n_peoples):
    i = 0
    res = 0
    while i < len(delta):
        if delta[i] <= porog:
            res += 1
            i += n_peoples - 1
        i += 1
    return res


def main(q_groups, n_peoples, peoples_lens):
    peoples_lens.sort()
    left_ans = 0
    right_ans = peoples_lens[-1] - peoples_lens[0]
    delta = [None] * (len(peoples_lens) - n_peoples + 1)
    for i in range(len(peoples_lens) - n_peoples + 1):
        delta[i] = peoples_lens[i + n_peoples - 1] - peoples_lens[i]
    while right_ans > left_ans:
        middle_ans = (left_ans + right_ans) // 2
        groups = calc_group(delta, middle_ans, n_peoples)
        if groups < q_groups:
            left_ans = middle_ans + 1
        else:
            right_ans = middle_ans
    return right_ans


if __name__ == '__main__':
    n, groups, group_peoples = list(map(int, input().split()))
    peoples_lens = []
    for i in range(n):
        peoples_lens.append(int(input()))
    res = main(groups, group_peoples, peoples_lens)
    print(res)


    assert main(2, 3, [170, 205, 225, 190, 260, 130, 225, 160])
