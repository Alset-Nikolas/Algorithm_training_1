def main(points, events):
    if len(events) == 0:
        return " ".join(["0"] * len(points))
    for point in points:
        events.append([point, "1look"])
    events.sort()
    res = dict()
    all_segments = 0
    for val_x, flag in events:
        if flag == "0open":
            all_segments += 1
        if flag == "1look":
            res[val_x] = all_segments
        if flag == "2close":
            all_segments -= 1
    return ' '.join([str(res[p_i]) for p_i in points])


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    events = []
    for _ in range(n):
        open_event, close_event = list(map(int, input().split()))
        events.append([min(open_event, close_event), "0open"])
        events.append([max(open_event, close_event), "2close"])
    points = list(map(int, input().split()))
    res = main(points, events)
    print(res)

    assert main([1, 6],
                [[0, '0open'], [5, '2close'], [-3, '0open'], [2, '2close'], [7, '0open'], [10, '2close']]) == "2 0"
    assert main([1, 2, 3, 4, 5, 6, 7, 8], [[2, '0open'], [4, '2close']]) == "0 1 1 1 0 0 0 0"
    assert main([1, 2, 3], [[2, '0open'], [2, '2close']]) == "0 1 0"
    assert main([5, 6, 7, 8, 9],
                [[5, '0open'], [10, '2close'], [6, '0open'], [9, '2close'], [7, '0open'], [8, '2close']]) == "1 2 3 3 2"
    assert main([2], [[0, '0open'], [2, '2close'], [2, '0open'], [4, '2close']]) == "2"
    assert main([2], [[0, '0open'], [2, '2close'], [2, '0open'], [2, '2close'], [2, '0open'], [4, '2close']]) == '3'
    assert main([5, 6, 7, 8, 9],
                [[5, '0open'], [10, '2close'], [5, '0open'], [9, '2close'], [5, '0open'], [8, '2close'], [5, '0open'],
                 [7, '2close'], [5, '0open'], [6, '2close']]) == "5 5 4 3 2"
    assert main([9, 8, 7, 6, 5],
                [[5, '0open'], [10, '2close'], [5, '0open'], [9, '2close'], [5, '0open'], [8, '2close'], [5, '0open'],
                 [7, '2close'], [5, '0open'], [6, '2close']]) == "2 3 4 5 5"
