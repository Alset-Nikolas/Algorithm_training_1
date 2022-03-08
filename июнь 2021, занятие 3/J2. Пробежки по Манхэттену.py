def increase(rect, n):
    X_plus_Y_max, X_minus_Y_min, X_plus_Y_min, X_minus_Y_max = rect
    return [X_plus_Y_max + n, X_minus_Y_min + n, X_plus_Y_min - n, X_minus_Y_max - n]


def impose(rect, rect2):
    X_plus_Y_max, X_minus_Y_min, X_plus_Y_min, X_minus_Y_max = rect
    X_plus_Y_max_2, X_minus_Y_min_2, X_plus_Y_min_2, X_minus_Y_max_2 = rect2
    return [min(X_plus_Y_max, X_plus_Y_max_2), min(X_minus_Y_min, X_minus_Y_min_2), max(X_plus_Y_min, X_plus_Y_min_2),
            max(X_minus_Y_max, X_minus_Y_max_2)]


def main(t, d, n):
    RecStart = [0, 0, 0, 0]

    for _ in range(n):
        RecStart = increase(rect=RecStart, n=t)
        x_new, y_new = list(map(int, input().split()))
        RecNew = increase([x_new + y_new, x_new - y_new, x_new + y_new, x_new - y_new], d)
        RecStart = impose(RecStart, RecNew)
    X_plus_Y_max, X_minus_Y_min, X_plus_Y_min, X_minus_Y_max = RecStart

    otvet = []

    A1, B1 = min(X_plus_Y_min, X_plus_Y_max), max(X_plus_Y_min, X_plus_Y_max)
    A2, B2 = min(X_minus_Y_min, X_minus_Y_max), max(X_minus_Y_min, X_minus_Y_max)
    for x_plus_y in range(A1, B1 + 1, 1):
        for x_minus_y in range(A2, B2 + 1, 1):
            x = x_plus_y + x_minus_y
            if x % 2 == 0:
                y = x_plus_y - x // 2
                otvet.append([x // 2, y])
    print(len(otvet))
    for x, y in otvet:
        print(f"{x} {y}")


if __name__ == '__main__':
    t, d, n = list(map(int, input().split()))
    main(t, d, n)
