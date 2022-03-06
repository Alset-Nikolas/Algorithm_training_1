import math

K1, M, K2, P2, N2 = map(int, (input().split()))


def find_options_quantity_apartments(M, K2, P2, N2):
    n_min = (K2 // ((P2 - 1) * M + N2))
    n_max = (K2 - 1) // ((P2 - 1) * M + N2 - 1)
    n_vars = []
    # print(range(n_min, n_max+1, 1))
    for n in range(n_min, n_max + 1, 1):
        if n != 0 and (M * (P2 - 1) + N2 - 1) * n + (K2 - 1) % n == K2 - 1:
            n_vars.append(n)
    return n_vars


def find_answer(K1, M, K2, P2, N2):
    if N2 > M or N2 <= 0:
        return [-1, -1]

    if P2 == 1 and N2 == 1:
        if K2 >= K1:
            return [1, 1]
        n_vars = range(K2, K1 + 1, 1)
    else:
        n_vars = find_options_quantity_apartments(M, K2, P2, N2)

    result = [-1, -1]
    for n_i in n_vars:
        floor_index = ((K1 - 1 - (K1 - 1) % n_i) / n_i) + 1
        n1 = floor_index % M
        p1 = ((floor_index - n1) / M) + 1
        # Если оказалось, что квартира на нулевом этаже,
        # то берём последний этаж предыдущего подъезда
        if n1 == 0:
            n1 = M
            p1 -= 1
        if result == [-1, -1]:
            result = [p1, n1]
        else:
            # Если для разных q, существует более одного значения подъезда или этажа, то значит,
            # что определить подъезд или этаж нельзя, ответ 0.
            if p1 != result[0]:
                result[0] = 0
            if n1 != result[1]:
                result[1] = 0
    return list(map(int, result))


assert find_answer(89, 20, 41, 1, 11) == [2, 3]
assert find_answer(11, 1, 1, 1, 1) == [0, 1]
assert find_answer(3, 2, 2, 2, 1) == [-1, -1]
assert find_answer(16, 2, 15, 2, 1) == [2, 0]
assert find_answer(17, 2, 15, 2, 1) == [2, 0]
assert find_answer(18, 2, 15, 2, 1) == [2, 0]
assert find_answer(19, 2, 15, 2, 1) == [2, 0]
assert find_answer(20, 2, 15, 2, 1) == [2, 0]
assert find_answer(21, 2, 15, 2, 1) == [0, 0]
assert find_answer(22, 2, 15, 2, 1) == [0, 0]
assert find_answer(23, 2, 15, 2, 1) == [0, 0]
assert find_answer(24, 2, 15, 2, 1) == [0, 0]
assert find_answer(25, 2, 15, 2, 1) == [0, 0]
assert find_answer(26, 2, 15, 2, 1) == [0, 0]
assert find_answer(27, 2, 15, 2, 1) == [0, 0]
assert find_answer(28, 2, 15, 2, 1) == [0, 0]
assert find_answer(29, 2, 15, 2, 1) == [3, 0]
assert find_answer(5, 20, 2, 1, 1) == [1, 0]
assert find_answer(20, 20, 2, 1, 1) == [1, 0]
assert find_answer(21, 20, 2, 1, 1) == [1, 0]
assert find_answer(753, 10, 1000, 1, 1) == [1, 1]
assert find_answer(10, 3, 50, 1, 50) == [-1, -1]
assert find_answer(25, 3, 1, 1, 1) == [0, 0]
assert find_answer(25, 3, 1, 1, 1) == [0, 0]
assert find_answer(24, 3, 1, 1, 1) == [0, 0]
assert find_answer(23, 3, 1, 1, 1) == [0, 0]
assert find_answer(22, 3, 1, 1, 1) == [0, 0]
assert find_answer(21, 3, 1, 1, 1) == [0, 0]
assert find_answer(20, 3, 1, 1, 1) == [0, 0]
assert find_answer(19, 3, 1, 1, 1) == [0, 0]
assert find_answer(18, 3, 1, 1, 1) == [0, 0]
assert find_answer(17, 3, 1, 1, 1) == [0, 0]
assert find_answer(16, 3, 1, 1, 1) == [0, 0]
assert find_answer(15, 3, 1, 1, 1) == [0, 0]
assert find_answer(19, 3, 8, 1, 1) == [1, 0]
assert find_answer(19, 3, 7, 1, 1) == [1, 0]
assert find_answer(19, 3, 6, 1, 1) == [0, 0]
assert find_answer(18, 3, 6, 1, 1) == [1, 0]
assert find_answer(6, 3, 18, 1, 1) == [1, 1]
assert find_answer(3, 1, 9, 7, 3) == [-1, -1]
assert find_answer(3, 1, 2, 1, 1) == [0, 1]
assert find_answer(2, 1, 1, 1, 1) == [0, 1]
assert find_answer(3, 2, 2, 1, 1) == [1, 0]
assert find_answer(2, 3, 1, 1, 1) == [1, 0]
assert find_answer(842887, 10, 163729, 24, 8) == [123, 0]
assert find_answer(20, 10, 4, 1, 5) == [-1, -1]
assert find_answer(20, 10, 5, 1, 5) == [2, 10]
assert find_answer(11, 2, 4, 1, 2) == [0, 2]

print(*find_answer(K1, M, K2, P2, N2))
