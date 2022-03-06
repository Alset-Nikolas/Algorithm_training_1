def fink(mode, troom, tcond):
    if mode == "fan":
        print(troom)
    elif mode == "auto":
        print(tcond)
    elif mode == "heat":
        if troom <= tcond:
            print(tcond)
        else:
            print(troom)
    elif mode == "freeze":
        if troom > tcond:
            print(tcond)
        else:
            print(troom)


def main():
    troom, tcond = map(int, input().split())
    mode = input()
    fink(mode, troom, tcond)


if __name__ == "__main__":
    main()
