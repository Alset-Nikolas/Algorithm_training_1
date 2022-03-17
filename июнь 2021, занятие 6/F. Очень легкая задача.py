def func_T(parametrs, n):
    '''Зависимость времени от количества деталей, которые делает медленный принтер'''
    N, t_fast, t_slow = parametrs
    return max(t_fast * (N - n), t_slow * n)


def calk_opt_n(parametrs):
    '''Оптимальное количество деталей для медленного принтера для времени T'''
    N, t_fast, t_slow = parametrs
    n_min = 0
    n_max = N
    while n_max > n_min:
        n_middle = (n_min + n_max) // 2
        if func_T(parametrs, n_middle) <= func_T(parametrs, n_middle + 1):
            n_max = n_middle
        else:
            n_min = n_middle + 1
    return n_min


def calc_answer(t_fast, t_slow, N):
    parametrs = N, t_fast, t_slow
    n_opt = calk_opt_n(parametrs)
    return func_T(parametrs, n_opt)




def main(N, x, y):
    t_fast = min(x, y)
    if N == 1:
        return t_fast
    N -= 1
    t_fast = min(x, y)
    t_slow = max(x, y)
    return t_fast + calc_answer(t_fast, t_slow, N)


if __name__ == '__main__':
    N, t_fast, t_slow = list(map(int, input().split()))
    res = main(N, t_fast, t_slow)
    print(res)

    assert main(4, 1, 1) == 3
    assert main(5, 1, 2) == 4
    assert main(10, 1, 11) == 10
