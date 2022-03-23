

def main(event):
    now_person = []
    start = None
    end = None
    last_val = None
    for i, event_i in enumerate(event):
        val, flag, name_index = event_i
        if i == 0 and val != 0:
            return "Wrong Answer"
        if i == len(event) - 1 and val!= 10000:
            return "Wrong Answer"

        if i != 0 and len(now_person) == 0:
            if val != last_val:
                return "Wrong Answer"

        if flag == "die":
            if now_person[0] == name_index:
                now_person = now_person[1:]
            else:
                return "Wrong Answer"
            if end is not None and end >= val :
                return "Wrong Answer"
            end = val

        if flag == "burn":
            now_person.append(name_index)
            if len(now_person) > 2:
                return "Wrong Answer"
            if start is not None and start >= val:
                return "Wrong Answer"
            start = val
        last_val = val
    return 'Accepted'


if __name__ == '__main__':
    n = int(input())
    for j in range(n):
        events_list = []
        info = list(map(int, input().split()))
        k = info[0]
        for i in range(1, 2 * k + 1, 2):
            event = [info[i], "burn", i // 2]
            events_list.append(event)
            event = [info[i + 1], "die", i // 2]
            events_list.append(event)

        events_list.sort()
        res = main(events_list)
        print(res)


