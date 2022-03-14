import math


def main(k, cards):
    res = 0
    collector = dict()
    for x in cards:
        if x not in collector:
            collector[x] = 0
        collector[x] += 1
    collector_keys = sorted(collector.keys())
    right_index = 0
    dublicate = 0
    for left_index, el in enumerate(collector_keys):
        while right_index < len(collector_keys) and collector_keys[right_index] <= k * el:
            if collector[collector_keys[right_index]] > 1:
                dublicate += 1
            right_index += 1
        #Все разные, но точно взяли el
        delta = right_index - left_index - 1
        res += 3 * delta * (delta-1)
        if collector[el] > 1:
            #тогда можно взять 2 элемента el
            res += 3 * delta
        if collector[el] > 2:
            # тогда можно взять 3 элемента el
            res += 1
        #нужно учесть парные не el варианты
        if collector[el] > 1:
            dublicate -= 1
        res += 3 * dublicate
    return res



if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    cards = list(map(int, input().split()))
    res = main(k, cards)
    print(res)

    assert main(2, [1, 1, 2, 2, 3]) == 9

