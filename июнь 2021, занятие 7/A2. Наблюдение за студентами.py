def main(N, teachers_look):
    teachers_look.sort(key=lambda x: x[0])
    res = 0
    if len(teachers_look) == 0:
        return N

    start, end = teachers_look[0]
    if start > 0:
        res += start

    last_person = end
    if len(teachers_look) >1:
        for i in range(1, len(teachers_look)):
            start_before, end_before = teachers_look[i - 1]
            start_after, end_after = teachers_look[i]
            if end_after < end_before:
                teachers_look[i][1] = end_before
            if start_after - end_before > 0:
                res += start_after - end_before - 1
            last_person = max(last_person, end_before)
        last_person = max(last_person, end_after)
    if last_person < N - 1:
        res += N - 1 - last_person
    return res


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    teachers = []
    for i in range(M):
        teachers.append(list(map(int, input().split())))
    res = main(N, teachers)
    print(res)
    assert main(10, [[9, 9], (2, 4), [1, 3]]) == 5
    assert main(10, [[1, 1], [1, 2]]) == 8
    assert main(1, [[0, 0]]) == 0

