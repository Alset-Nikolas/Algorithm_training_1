import math


def main(powers, models):
    res = 0
    models.sort(key=lambda x: x[0])
    powers.sort()
    for i in range(len(models) - 1, 0, -1):
        if models[i][1] <= models[i - 1][1]:
            models[i - 1] = models[i]
    left = 0
    for power in powers:
        while left < len(models) and models[left][0] < power:
            left += 1
        res += models[left][1]
    return res


if __name__ == '__main__':
    res = 0
    n = int(input())
    powers = list(map(int, input().split()))
    m = int(input())
    models = [0] * m
    for i in range(m):
        models[i] = list(map(int, input().split()))

    res = main(powers, models)
    print(res)
