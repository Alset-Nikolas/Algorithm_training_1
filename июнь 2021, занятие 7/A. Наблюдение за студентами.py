def main(N, teacher_look):
    students = [1] * N
    for (start, end) in teacher_look:
        for i in range(start,end+1):
            students[i] = 0
    return sum(students)


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    teachers = []
    for i in range(M):
        teachers.append(tuple(map(int, input().split())))
    res = main(N, teachers)
    print(res)

    assert main(10, [(1,3), (2,4), (9,9)]) == 5
    assert main(10, [(1, 1), (1, 2)]) == 8
