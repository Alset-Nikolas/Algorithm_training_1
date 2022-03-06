def add_info(f_answer, fl, fr):
    if fl > f_answer[0]:
        f_answer[0] = fl
    if fr < f_answer[1]:
        f_answer[1] = fr

def search(N, info):
    f_start = info[0][0]
    f_old = f_start
    f_info_old = None
    f_answer = [30, 4000]
    fl = 30
    fr = 4000
    for i in range(1, N):
        f_now = info[i][0]
        dist = abs(f_old - f_now)
        if f_now == f_old:
            continue
        if info[i][1] == "closer":
            if f_now < f_old:
                fr = f_now + dist / 2
            else:
                fl = f_now - dist / 2
        else:
            if f_now > f_old:
                fr = f_now - dist / 2
            else:
                fl = f_now + dist / 2
        add_info(f_answer, fl, fr)
        f_old = f_now

    if f_answer[0] < 30:
        f_answer[0] = 30
    if f_answer[1] > 4000:
        f_answer[1] = 4000
    if f_answer[1] < f_answer[0]:
        f_answer[0], f_answer[1] =f_answer[1], f_answer[0]
    return f_answer


def main():
    n = int(input())
    info = []
    for i in range(n):
        if i == 0:
            info.append([float(input()), ''])
        else:
            new = input().split()
            info.append([float(new[0]), new[1]])
    res = search(n, info)
    print(*res)


if __name__ == "__main__":
    main()

    assert search(3, [[440, ''], [220, 'closer'], [300, "further"]]) == [30.0, 260.0]
    assert search(4, [[554, ''], [880, 'further'], [440, "closer"], [622, "closer"]]) == [531.0, 660.0]
    assert search(1, [[554, '']]) == [30, 4000]

    assert search(5, [[3072.7508920475825, ''], [3087.2740875071913, "further"], [2376.1007719516238, "further"], [2376.1007719516238, "further"], [3719.8803250966535, "further"], [1575.5506732924753, "further"]]) == [2731.6874297294075, 3047.990548524139
]
