def count_small_x(list_A, x):
    '''Кол-во элементов строго меньше x'''
    i_left = 0
    i_right = len(list_A)
    while i_right > i_left:
        middle_i = (i_right + i_left) // 2
        if list_A[middle_i] >= x:
            i_right = middle_i
        else:
            i_left = middle_i + 1
    return i_left


def count_big_x(list_A, x):
    '''Кол-во элементов строго больше x'''
    i_left = 0
    i_right = len(list_A)
    while i_right > i_left:
        middle_i = (i_right + i_left) // 2
        if list_A[middle_i] <= x:
            i_left = middle_i + 1
        else:
            i_right = middle_i
    return len(list_A) - i_left


def calc_item(k, A, B):
    min_x = min(A[0], B[0])
    max_x = max(A[-1], B[-1])
    L = len(A)
    while min_x < max_x:
        middle_x = (max_x + min_x) // 2
        left_numbers = count_small_x(A, middle_x) + count_small_x(B, middle_x)
        right_numbers = count_big_x(A, middle_x) + count_big_x(B, middle_x)
        if left_numbers < L and right_numbers <= L:
            return middle_x
        if right_numbers > L:
            min_x = middle_x + 1
        if left_numbers >= L:
            max_x = middle_x - 1
    return min_x


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    data = [[] for x in range(n)]
    for i in range(n):
        x1, d1, a, c, m = list(map(int, input().split()))
        d = [d1] * k
        x = [x1] * k
        for j in range(1, k):
            d[j] = (a * d[j - 1] + c) % m
            x[j] = x[j - 1] + d[j - 1]
        data[i] = x

        del x, x1, d, d1, a, c, m

    for i in range(n):
        for j in range(i + 1, n):
            print(calc_item(k, data[i], data[j]))
        data[i] = []
