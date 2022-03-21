def main(events, N):
    working_class = set()
    res_minuts = 0
    for event in events:
        minuts, flag, index_class = event
        if flag == "0_open":
            working_class.add(index_class)
            if len(working_class) == N:
                start_time_all = minuts


        if flag == "1_close" and index_class in working_class:
            if len(working_class) == N:
                res_minuts += minuts - start_time_all
            working_class.remove(index_class)
    return res_minuts

if __name__ == '__main__':
    n = int(input())
    events = []
    for i in range(n):
        time_start_hour, time_start_minut, time_end_hour, time_end_minut = list(map(int, input().split()))
        minut_start = time_start_hour * 60 + time_start_minut
        minut_end = time_end_hour * 60 + time_end_minut
        if minut_start < minut_end:
            event_day_open = [minut_start, "0_open", i]
            event_day_close = [minut_end, "1_close", i]
            events.append(event_day_open)
            events.append(event_day_close)
        elif minut_start == minut_end:
            event_day_open = [0, "0_open", i]
            event_day_close = [1440, "1_close", i]
            events.append(event_day_open)
            events.append(event_day_close)
        else:
            event_day_open = [0, "0_open", i]
            event_day_close = [minut_end, "1_close", i]
            events.append(event_day_open)
            events.append(event_day_close)

            event_day_open = [minut_start, "0_open", i]
            event_day_close = [1440, "1_close", i]
            events.append(event_day_open)
            events.append(event_day_close)

    events.sort()
    res = main(events, n)
    print(res)
