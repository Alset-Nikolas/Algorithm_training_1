import datetime


def main(events):
    ans = []
    nabor = set()
    for time_val, flag, index_name in events:
        if flag == "1_burn_person":
            nabor.add(index_name)
        if flag == "0_die_person":
            flag = True
            for i, ans_i in enumerate(ans):
                if nabor | ans_i == nabor and len(ans_i) < len(nabor):
                    ans[i] = nabor
                    break
                if ans_i | nabor == ans_i:
                    flag = False
                    break
            if flag:
                ans.append(nabor.copy())
            nabor.remove(index_name)
    if ans == []:
        return 0
    return ans


if __name__ == '__main__':
    n = int(input())
    events = []
    for i in range(n):
        day_burn, month_burn, year_burn, day_die, month_die, year_die = list(map(int, input().split()))
        burn = datetime.datetime(day=day_burn, month=month_burn, year=year_burn).date()
        burn = burn.replace(year=burn.year + 18)
        die = datetime.datetime(day=day_die, month=month_die, year=year_die).date()
        end_ = burn.replace(year=burn.year + 62) - datetime.timedelta(days=1)
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
