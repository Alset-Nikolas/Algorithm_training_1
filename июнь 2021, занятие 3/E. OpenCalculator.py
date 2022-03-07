def main(x, y, z, number):
    return len(set(number) - set([x, y, z]))


if __name__ == '__main__':
    x, y, z = input().split()
    number = input()
    res = main(x, y, z, number)
    print(res)



    assert main("1", "2", "3", "1123") == 0
    assert main("1", "2", "3", "1001") == 1
    assert main("5", "7", "3", '123') == 2