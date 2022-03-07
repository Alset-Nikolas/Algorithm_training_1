def pprint(res):
    for len_set, res_items in res:
        print(len_set)
        for x in res_items:
            print(x)


def main(info):
    all_know = set()
    all_languages = set()
    for i, languages in enumerate(info):
        len_s = set(languages)
        if i == 0:
            all_know=len_s
        else:
            all_know = all_know & len_s
        all_languages = all_languages | len_s
    answer = [[len(all_know), sorted(list(all_know))], [len(all_languages), sorted(list(all_languages))]]
    return answer



if __name__ == '__main__':
    n = int(input())
    info = []
    for x in range(n):
        k = int(input())
        new_el = []
        for k_ in range(k):
            new_el.append(input())
        info.append(new_el)
    res = main(info)
    pprint(res)

    assert main([['Russian', 'English', 'Japanese'], ['Russian', 'English'], ['English']]) == [[1, ['English']], [3, ['English', 'Japanese', 'Russian']]]
    assert main([['Russian'], ['Russian'], ['English']]) == [[0, []], [2, ['English', 'Russian']]]
    assert main([['Russian'], [], ['English']]) == [[0, []], [2, ['English', 'Russian']]]