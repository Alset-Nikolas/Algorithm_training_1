def main(mass):
    for i in range(len(mass) - 1):
        if mass[i + 1] <= mass[i]:
            return "NO"
    return "YES"



if __name__ == '__main__':
    mass = list(map(int, input().split()))
    res = main(mass)
    print(res)



    assert main([1, 7, 9]) == "YES"
    assert main([1, 9, 7]) == "NO"
    assert main([2, 2, 2]) == "NO"
