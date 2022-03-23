def main(n, total_S, events):

    now_bloks = set()
    now_S = 0
    min_bloks = n + 1
    for event in events:
        z, flag, s, index_block = event
        if flag == "1_open":
            now_bloks.add(index_block)
            now_S += s

        if flag == "0_close":
            now_bloks.remove(index_block)
            now_S -= s
        if total_S == now_S and min_bloks > len(now_bloks):
            min_bloks = len(now_bloks)
    return min_bloks

if __name__ == '__main__':
    n, W, L = list(map(int, input().split()))
    events = []
    for i in range(n):
        x1, y1, z1, x2, y2, z2 = list(map(int, input().split()))
        s = abs(x1-x2) * abs(y1-y2)
        events.append([z1,"1_open", s, i+1])
        events.append([z2,"0_close", s, i+1])

    events.sort()
    WIN_bloks = main(n, L*W, events)
    if WIN_bloks ==n+1:
        print("NO")
    else:
        print("YES")
        print(WIN_bloks)
        now_bloks = set()
        now_S = 0
        min_bloks = n + 1
        for event in events:
            z, flag, s, index_block = event
            if flag == "1_open":
                now_bloks.add(index_block)
                now_S += s

            if flag == "0_close":
                now_bloks.remove(index_block)
                now_S -= s
            if W*L == now_S and min_bloks > len(now_bloks):
                min_bloks = len(now_bloks)
                if min_bloks == WIN_bloks:
                    print(*now_bloks)
                    break
