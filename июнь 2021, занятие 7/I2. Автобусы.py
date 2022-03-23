import datetime

if __name__ == '__main__':

    n_country, m_bus_reis = list(map(int, input().split()))
    all_bus = [0, 0]
    events = []
    for new_reis in range(m_bus_reis):
        first_country, time_run, second_country, time_stop = input().split()
        time_run = time_run.split(":")
        time_stop = time_stop.split(":")
        if time_run > time_stop:
            events.append([datetime.time(hour=int(time_run[0]), minute=int(time_run[1])), "1_go", int(first_country)])
            events.append([datetime.time(hour=23, minute=59, second=59), "0_stop", 0])
            events.append([datetime.time(hour=0), "1_go", 0])
            events.append([datetime.time(hour=int(time_stop[0]), minute=int(time_stop[1])), "0_stop", int(second_country)])
        else:
            events.append([datetime.time(hour=int(time_run[0]), minute=int(time_run[1])), "1_go", int(first_country)])
            events.append([datetime.time(hour=int(time_stop[0]), minute=int(time_stop[1])), "0_stop",  int(second_country)])
    del m_bus_reis, new_reis, first_country, time_run, second_country, time_stop
    events.sort()
    all_bus = 0
    country_bus = [0] * (n_country + 1)
    country_bus_flag = [0] * (n_country + 1)
    for event in events:
        time_val, flag, country = event
        if flag == "1_go":
            if country_bus[country] == 0:
                all_bus += 1
                country_bus[country] += 1
            country_bus[country] -= 1
            country_bus_flag[country] += 1
        if flag == "0_stop":
            country_bus[country] += 1
            country_bus_flag[country] -= 1
    print(all_bus if all([x == 0 for x in country_bus_flag]) else -1)
