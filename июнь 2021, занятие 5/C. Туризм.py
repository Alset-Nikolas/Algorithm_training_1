def main(coords, track):
    Y_LR = [0] * len(coords)
    Y_RL = [0] * len(coords)
    for i in range(1, len(coords), 1):
        dy_LR = coords[i][1] - coords[i - 1][1]
        if dy_LR > 0:
            Y_LR[i] = Y_LR[i - 1] + dy_LR
        else:
            Y_LR[i] = Y_LR[i - 1]
        dy_RL = coords[-i - 1][1] - coords[-i][1]
        if dy_RL > 0:
            Y_RL[-i - 1] = Y_RL[-i] + dy_RL
        else:
            Y_RL[-i - 1] = Y_RL[-i]
    # print(Y_LR)
    # print(Y_RL)

    #
    for n_1, n_2 in track:
        if n_1 < n_2:
            res = Y_LR[n_2-1] - Y_LR[n_1-1]
        else:
            res = Y_RL[n_2-1] - Y_RL[n_1-1]
        print(res)


if __name__ == '__main__':
    n = int(input())
    coords = []
    for x in range(n):
        coords.append(list(map(int, input().split())))

    m = int(input())
    track = []
    for x in range(m):
        track.append(list(map(int, input().split())))
    res = main(coords, track)
