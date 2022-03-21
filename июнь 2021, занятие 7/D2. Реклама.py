def calc_max_group(events):
    best_people_saw = 0
    peoples_look_first_video = set()
    best_time_1 = 0
    best_time_2 = 0

    if len(events) == 0:
        return 0, 5, 10
    if len(events) == 2:
        return 1, events[0][0], events[0][0] + 5
    for i in range(len(events)):
        time_event_i, prioritet, name_index_i, flag_i = events[i]
        if flag_i == "came":
            peoples_look_first_video.add(name_index_i)
            if len(peoples_look_first_video) > best_people_saw:
                best_people_saw = len(peoples_look_first_video)
                best_time_1 = time_event_i
                best_time_2 = best_time_1 + 5

        count_peoples_look_second_video = 0
        for j in range(i, len(events)):
            time_event_j, prioritet, name_index_j, flag_j = events[j]
            if flag_j == "came" and name_index_j not in peoples_look_first_video:
                count_peoples_look_second_video += 1
            if time_event_j - time_event_i >= 5 and len(
                    peoples_look_first_video) + count_peoples_look_second_video > best_people_saw:
                best_people_saw = len(peoples_look_first_video) + count_peoples_look_second_video
                best_time_1 = time_event_i
                best_time_2 = time_event_j
            if flag_j == "gone" and name_index_j not in peoples_look_first_video:
                count_peoples_look_second_video -= 1
        if flag_i == "gone":
            peoples_look_first_video.remove(name_index_i)
    return best_people_saw, min(best_time_1, best_time_2), max(best_time_1, best_time_2)


def main(times):
    events = []
    for i, time in enumerate(times):
        start, end = time
        if end - start < 5:
            continue
        events.append([start, 1, i, "came"])
        events.append([end - 5, 2, i, "gone"])
    events.sort()
    return calc_max_group(events)


if __name__ == '__main__':
    n = int(input())
    times = []
    for i in range(n):
        times.append(list(map(int, input().split())))
    res = main(times)
    print(*res)
