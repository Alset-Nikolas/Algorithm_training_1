import datetime


def main(events):
    ans = []
    nabor_now = set()
    flag_del = True
    for time_val, flag, index_name in events:
        if flag == "1_burn_person":
            nabor_now.add(index_name)
            flag_del = True
        if flag == "0_die_person":
            if flag_del:
                ans.append(nabor_now.copy())
                flag_del = False
            nabor_now.remove(index_name)

    if ans == []:
        return 0
    return set([tuple(x) for x in ans])


if __name__ == '__main__':
    n = int(input())
    events = []
    for i in range(n):
        day_burn, month_burn, year_burn, day_die, month_die, year_die = list(map(int, input().split()))
        burn = datetime.datetime(day=day_burn, month=month_burn, year=year_burn).date()
        burn = burn.replace(year=burn.year + 18)
        die = datetime.datetime(day=day_die, month=month_die, year=year_die).date()
        end_ = burn.replace(year=burn.year + 62)
        if burn < die:
            events.append([burn, "1_burn_person", i + 1])
            if die > end_:
                events.append([end_, "0_die_person", i + 1])
            else:
                events.append([die, "0_die_person", i + 1])
    events.sort()
    res = main(events)
    if res == 0:
        print(0)
    else:
        for x in res:
            print(*x)

'''мой > 2186'''
'''правильный ответ -> 389171'''
