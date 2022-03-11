def main(SUMMA, cars):
    res = 0
    sum_ = 0
    left_index = 0
    for car_number in cars:
        sum_ += car_number
        while sum_ > SUMMA:
            sum_ -= cars[left_index]
            left_index += 1
        if sum_ == SUMMA:
            res += 1
    return res


if __name__ == '__main__':
    N, SUMMA = list(map(int, input().split()))
    cars = list(map(int, input().split()))
    res = main(SUMMA, cars)
    print(res)
    
    assert main(17, [17, 7, 10, 7, 10]) == 4
    assert main(10, [1, 2, 3, 4, 1]) == 2