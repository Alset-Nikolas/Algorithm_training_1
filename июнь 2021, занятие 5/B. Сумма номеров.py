with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            n, summa = list(map(int, line.split()))
        else:
            cars = list(map(int, line.split()))
prefix_sum = [0]
res = 0

for i in range(len(cars)):
    j = i
    while j < len(prefix_sum) and prefix_sum[j] - prefix_sum[i] < summa:
        j += 1
        if j == len(prefix_sum) and j != len(cars) + 1:
            prefix_sum.append(prefix_sum[j - 1] + cars[j - 1])
    if j != len(prefix_sum):
        if prefix_sum[j] - prefix_sum[i] == summa:
            res += 1
with open("output.txt", "w") as f:
    f.write(str(res))
