import math


def main(k, text):
    max_len = 0
    number = 0
    collector = dict()
    left_index = 0
    for right_index, el in enumerate(text):
        if el not in collector:
            collector[el] = 0
        collector[el] += 1
        if collector[el] > k or right_index == len(text) - 1:
            if collector[el] > k:
                new_len = right_index - left_index
            else:
                new_len = right_index - left_index + 1
            if new_len > max_len:
                max_len = new_len
                number = left_index + 1
            while collector[el] > k:
                collector[text[left_index]] -= 1
                left_index += 1

    return [max_len, number]


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    text = input()
    res = main(k, text)
    print(*res)
    assert main(1, "abb") == [2, 1]
    assert main(2, "ababa") == [4, 1]
    assert main(3, "aaabbbcccc") == [9, 1]
    assert main(3, "aaabbbccccaaabbbddd") == [12, 8]
    assert main(3, "aaabbbccccaaabbbdddd") == [12, 8]
    assert main(3, "aaabbbccccaaabbbddddd") == [12, 8]
