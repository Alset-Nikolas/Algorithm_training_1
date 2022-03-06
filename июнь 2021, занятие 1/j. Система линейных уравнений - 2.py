def possible_answer(delta, delta_x, delta_y):
    '''Есть ли решение этой системы?'''
    # if delta == 0 and delta_x != 0 and delta_y != 0:
    if delta != 0:
        # 1 решение
        return True
    if delta == 0 and delta_x == 0 and delta_y == 0:
        # бесконечно много или нет решения вообще
        return True
    return False


def one_answer(delta, delta_x, delta_y):
    '''Решение 1?'''
    if delta_x == 0 and delta_y == 0:
        return False
    return True


def my_format(number):
    if number - int(number) != 0:
        return number
    return int(number)


def trivial(a, b, e, c, d, f):
    if a == c and b == d:
        return True
    return False


def system_linear(a, b, e, c, d, f):
    if a == b == 0 or c == d  == 0:
        if a == b == 0 and e != 0:
            return False
        elif c == d == 0 and f != 0:
            return False
        return True
    if (a == 0 and c != 0) or (c == 0 and a != 0) or (b != 0 and d == 0) or (b == 0 and d != 0):
        return False
    if a != 0:
        c1 = b / a
        c2 = e / a
        c3 = d / c
        c4 = f / c
        return c1 == c3 and c2 == c4
    else:
        c2 = e / b
        c4 = f / d
        return c2 == c4


def main(a, b, e, c, d, f):
    delta = a * d - b * c
    delta_x = e * d - b * f
    delta_y = a * f - e * c

    if possible_answer(delta, delta_x, delta_y):
        if one_answer(delta, delta_x, delta_y):
            x1 = my_format(delta_x / delta)
            y1 = my_format(delta_y / delta)
            answer = f"2 {x1} {y1}"
        else:
            # ax+by=e
            # cx+dy=f
            if system_linear(a, b, e, c, d, f):
                if a == b == e == 0:
                    a, b, e = c, d, f
                if a == 0 and b == 0:
                    answer = f"5"
                elif a == 0:
                    res = my_format(e / b)
                    answer = f"4 {round(res, 5)}"
                elif b == 0:
                    res = my_format(e / a)
                    answer = f"3 {round(res, 5)}"
                else:
                    k = my_format(-a / b)
                    b = my_format(e / b)
                    answer = f"1 {round(k, 5)} {round(b, 5)}"
            else:
                answer = "0"
    else:
        answer = "0"

    return answer


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())
    answer = main(a, b, e, c, d, f)
    print(answer)

    assert main(a=1, b=0, c=0, d=1, e=3, f=3) == '2 3 3'
    assert main(a=1, b=1, c=2, d=2, e=1, f=2) == '1 -1 1'
    assert main(a=0, b=2, c=0, d=4, e=1, f=2) == '4 0.5'
    assert main(a=1, b=1, e=2, c=1, d=1, f=2) == '1 -1 2'
    assert main(a=0, b=0, e=0, c=0, d=0, f=0) == '5'
    assert main(a=1, b=1, e=2, c=1, d=1, f=3) == '0'
    assert main(a=0, b=1, e=2, c=0, d=1, f=2) == '4 2'
    assert main(a=1, b=0, e=2, c=1, d=0, f=2) == '3 2'
    assert my_format(1.1) == 1.1
    assert my_format(1.0) == 1
    assert my_format(-1.0) == -1
    assert my_format(-1.2) == -1.2
    assert my_format(0.2) == 0.2
    assert my_format(-0.2) == -0.2

    assert main(a=1, b=0, c=0, d=1, e=3, f=3) == "2 3 3"
    assert main(a=2, b=2, c=3, d=-3, e=6, f=-3) == "2 1 2"
    assert main(a=1, b=1, c=1, d=-1, e=3, f=-1) == "2 1 2"
    assert main(a=1, b=1, c=2, d=2, e=1, f=2) == "1 -1 1"
    assert main(a=1, b=1, c=1, d=1, e=1, f=2) == "0"
    assert main(a=0, b=1, c=0, d=1, e=2, f=3) == "0"
    assert main(a=0, b=1, c=0, d=2, e=2, f=4) == '4 2'
    assert main(a=1, b=0, c=2, d=0, e=2, f=4) == "3 2"
    assert main(a=0, b=0, c=0, d=0, e=0, f=0) == '5'
    assert main(a=0, b=0, c=0, d=0, e=1, f=0) == '0'
    assert main(a=0, b=2, c=0, d=4, e=1, f=2) == '4 0.5'
    assert main(a=0, b=2, c=0, d=4, e=1, f=2) == '4 0.5'
    assert main(a=0, b=0, c=2, d=4, e=0, f=2) == '1 -0.5 0.5'
    assert main(a=2, b=4, c=0, d=0, e=2, f=0) == '1 -0.5 0.5'
    assert main(a=2, b=0, c=3, d=0, e=2, f=3) == "3 1"
    assert main(a=2, b=2, c=3, d=0, e=6, f=3) == "2 1 2"
    assert main(a=1, b=1, c=1.5, d=0, e=3, f=1.5) == "2 1 2"
