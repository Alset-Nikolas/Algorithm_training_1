a = int(input())
b = int(input())
c = int(input())


def ODZ(x):
    if a >= 0 and x >= (-1) * b / a:
        return True
    elif a < 0 and x <= (-1) * b / a:
        return True
    return False


if a == 0:
    if (b > 0 and b ** 0.5 == c) or (b == 0 and c == 0):
        print('MANY SOLUTIONS')
    else:
        print("NO SOLUTION")
else:
    if c >= 0:
        x = (c ** 2 - b) / a
        if x == int(x) and ODZ(x):
            print(int(x))
        else:
            print("NO SOLUTION")
    else:
        print("NO SOLUTION")
