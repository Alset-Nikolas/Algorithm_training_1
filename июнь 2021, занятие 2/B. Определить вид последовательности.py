# По последовательности чисел во входных данных определите ее вид:
#
# CONSTANT – последовательность состоит из одинаковых значений
# ASCENDING – последовательность является строго возрастающей
# WEAKLY ASCENDING – последовательность является нестрого возрастающей
# DESCENDING – последовательность является строго убывающей
# WEAKLY DESCENDING – последовательность является нестрого убывающей
# RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов
# Формат ввода

def ascending(flag_ASCENDING, el_now, el_next):
    if flag_ASCENDING is not None and el_now < el_next:
        '''последовательность является строго возрастающей'''
        return True
    return None


def weakly_ascending(flag_WEAKLY_ASCENDING, el_now, el_next):
    if flag_WEAKLY_ASCENDING is not None and el_now <= el_next:
        '''последовательность является нестрого возрастающей'''
        return True
    return None


def desending(flag_DESCENDING, el_now, el_next):
    if flag_DESCENDING is not None and el_now > el_next:
        '''последовательность является строго убывающей'''
        return True
    return None


def weakly_desending(flag_WEAKLY_DESCENDING, el_now, el_next):
    if flag_WEAKLY_DESCENDING is not None and el_now >= el_next:
        '''последовательность является строго убывающей'''
        return True
    return None


def main(mass):
    if len(mass) == 0:
        return "RANDOM"
    len_list = len(mass)
    end_item = mass[-1]
    count_repeat = 1
    flag_ASCENDING = False
    flag_WEAKLY_ASCENDING = False
    flag_DESCENDING = False
    flag_WEAKLY_DESCENDING = False

    for i in range(len_list - 1):
        flag_ASCENDING = ascending(flag_ASCENDING, el_now=mass[i], el_next=mass[i + 1])
        flag_WEAKLY_ASCENDING = weakly_ascending(flag_WEAKLY_ASCENDING, el_now=mass[i], el_next=mass[i + 1])
        flag_DESCENDING = desending(flag_DESCENDING, el_now=mass[i], el_next=mass[i + 1])
        flag_WEAKLY_DESCENDING = weakly_desending(flag_WEAKLY_DESCENDING, el_now=mass[i], el_next=mass[i + 1])
        if end_item == mass[i]:
            count_repeat += 1

    if count_repeat == len_list:
        return "CONSTANT"
    if flag_ASCENDING:
        return 'ASCENDING'
    if flag_WEAKLY_ASCENDING:
        return 'WEAKLY ASCENDING'
    if flag_DESCENDING:
        return "DESCENDING"
    if flag_WEAKLY_DESCENDING:
        return "WEAKLY DESCENDING"
    return "RANDOM"


if __name__ == "__main__":
    end = -2000000000
    mass = []
    new_el = float(input())
    while new_el != end:
        mass.append(new_el)
        new_el = float(input())
    res = main(mass)
    print(res)

    assert main([-530, -530, -530, -530, -530, -530]) == "CONSTANT"
    assert main([1, 2, 3, 4, 5, 6, 7]) == "ASCENDING"
    assert main([1, 2, 2, 4, 5, 6, 7]) == "WEAKLY ASCENDING"
    assert main([0, 0, 2, 4, 5, 6, 7]) == "WEAKLY ASCENDING"
    assert main([0, -1, 2, 4, 5, 6, 7]) == "RANDOM"
    assert main([10, 9, 8, 6, 1, 0, -1]) == "DESCENDING"
    assert main([10, 9, 0, 6, 1, 0, -1]) == "RANDOM"
    assert main([0, 0, 0,0, 0, 0, -1]) == "WEAKLY DESCENDING"
