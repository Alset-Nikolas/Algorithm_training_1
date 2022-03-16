'''Если можно повернуть прямоуголоьники:'''


def main(w, h, n):
    start = 0
    end = (w + h) * n
    while end > start:
        middle = (start + end) // 2
        if middle ** 2 >= w * h * n:
            end = middle
        else:
            start = middle + 1

    return start


if __name__ == '__main__':
    w, h, n = list(map(int, input().split()))
    res = main(w, h, n)
    print(res)
