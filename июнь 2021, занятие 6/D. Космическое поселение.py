def main(n, a, b, w, h):
    d_left = 0
    d_right = max(w, h)
    while d_right-d_left!=1:
        d_center = (d_left + d_right) // 2
        # (a+2*d_center) * (b+2*d_center) * n > w*h
        if (w//(a+2*d_center)) * (h//(b+2*d_center)) >= n or (h//(a+2*d_center)) * (w//(b+2*d_center)) >= n:
            d_left = d_center
        else:
            d_right = d_center
    return d_left
if __name__ == '__main__':
    n, a, b, w, h = list(map(int, input().split()))
    res = main(n, a, b, w, h)
    print(res)
    assert main(1, 1, 1, 1, 1) == 0
    assert main(1, 1, 1, 3, 3) == 1
    assert main(1, 1, 1, 1000, 1) == 0
    assert main(2, 1, 1, 4, 4) == 0
    assert main(3, 1, 3, 3, 3) == 0
    assert main(3, 1, 1, 3, 9) == 1
    assert main(3, 1, 1, 9, 3) == 1
    assert main(3, 1, 2, 9, 4) == 1
    assert main(3, 1, 2, 4, 9) == 1