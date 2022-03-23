import datetime
'''Понятно, но по тестам не проходит (память/скорость)'''

def main(n_country, events):
    country_bus = dict()
    for i in range(n_country + 1):
        country_bus[i] = 0
    all_bus = [0, 0]
    for i in range(2):
        for event in events:
            time_val, flag, first_country, second_country, reis_number = event
            if flag == "1_go":
                if country_bus[first_country] == 0:
                    all_bus[i] += 1
                    country_bus[first_country] += 1
                country_bus[first_country] -= 1
            if flag == "0_stop":
                country_bus[second_country] += 1
    if all_bus[1] != 0:
        return -1
    return all_bus[0]


if __name__ == '__main__':
    n_country, m_bus_reis = list(map(int, input().split()))
    events = []
    for new_reis in range(m_bus_reis):
        first_country, time_run, second_country, time_stop = input().split()
        first_country = int(first_country)
        second_country = int(second_country)
        time_run = datetime.time(hour=int(time_run.split(":")[0]), minute=int(time_run.split(":")[1]))
        time_stop = datetime.time(hour=int(time_stop.split(":")[0]), minute=int(time_stop.split(":")[1]))
        if time_run > time_stop:
            events.append([time_run, "1_go", first_country, 0, new_reis])
            events.append([datetime.time(hour=23, minute=59, second=59), "0_stop", first_country, 0, new_reis])
            events.append([datetime.time(hour=0), "1_go", 0, second_country, new_reis])
            events.append([time_stop, "0_stop", 0, second_country, new_reis])
        else:
            events.append([time_run, "1_go", first_country, second_country, new_reis])
            events.append([time_stop, "0_stop", first_country, second_country, new_reis])
    events.sort()
    res = main(n_country, events)
    print(res)
