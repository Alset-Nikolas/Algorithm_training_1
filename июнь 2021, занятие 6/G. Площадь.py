def add_sloy(n, h, w):
    return 2*n*(w+h-2-2*(n-1))


def main(h, w, all_t):
    start_t = 0
    end_t = max(w, h) // 2
    while end_t > start_t:
        middle = (start_t + end_t + 1)//2
        if 2*middle*(w+h-2*middle) > all_t:
            end_t = middle - 1
        else:
            start_t = middle
    return end_t


if __name__ == '__main__':
    h = int(input())
    w = int(input())
    all_t = int(input())
    res = main(h, w, all_t)
    print(res)

    assert main(6, 7, 38) == 2

