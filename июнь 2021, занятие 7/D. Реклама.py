def main(times):
    events = []
    for i, time in enumerate(times):
        start, end = time
        if end - start < 5:
            continue
        events.append([start, 1, i, "came"])
        events.append([end, 2, i, "gone"])
    events.sort()
    now_people = dict()
    max_people = set()
    max_people_2 = set()
    ans_time = [1, 0]
    for i, event in enumerate(events):
        now_time, prioritet, index_person, flag = event

        if flag == "came":
            now_people[index_person] = now_time

        group = set()
        for person, time_start in now_people.items():
            if now_time - time_start >= 5:
                group.add(person)
        if len(max_people) < len(group):
            max_people_2 -= group
            if len(max_people - group) > len(max_people_2):
                max_people_2 = max_people - group
                ans_time[1] = ans_time[0]
            max_people = group
            ans_time[0] = now_time - 5
        else:
            if len(group-max_people) > len(max_people_2):
                max_people_2 = group - max_people
                ans_time[1] = now_time - 5

        if flag == "gone":
            now_people.pop(index_person)
    if ans_time[1] == 0:
        times.sort(key=lambda x: x[1])
        ans_time[1] = times[-1][1] + 10

    ans_time.sort()
    return len(max_people) + len(max_people_2), ans_time[0], ans_time[1]


if __name__ == '__main__':
    n = int(input())
    times = []
    for i in range(n):
        times.append(list(map(int, input().split())))
    res = main(times)
    print(*res)
    assert main([[1,1], [2,2]]) == (0,1,12)