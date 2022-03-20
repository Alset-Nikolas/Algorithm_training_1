def main(cords, D):
    vars = dict()
    events = []
    for cord in cords:
        events.append([cord, 0, "open_variant"])
        events.append([cord + D, 1,"close_variant"])
    events.sort()
    now_vars = set()
    free_vars = list()
    max_var = 0
    for event in events:
        val, pioritet_sort, flag = event
        if flag == "open_variant":
            if not free_vars and len(now_vars) == 0:
                vars[val] = 1
                max_var += 1
                now_vars.add(1)
                continue
            if free_vars:
                vars[val] = free_vars[0]
                free_vars.pop(0)
                now_vars.add(vars[val])
                continue
            max_var += 1
            new_var = max_var
            vars[val] = new_var
            now_vars.add(new_var)

        if flag == "close_variant":
            var_cord = vars[val - D]
            now_vars.remove(var_cord)
            free_vars.append(var_cord)

    return max_var, " ".join([str(vars[x]) for x in cords])

if __name__ == '__main__':
    n, d = list(map(int, input().split()))
    cords = list(map(int, input().split()))
    max_var, res = main(cords, d)
    print(max_var)
    print(res)