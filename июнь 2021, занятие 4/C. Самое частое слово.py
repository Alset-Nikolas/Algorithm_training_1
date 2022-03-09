def main(text):
    slova = dict()
    answer = []
    max_size = 0
    for el in text.split():
        if el not in slova:
            slova[el] = 0
        slova[el] += 1
        if max_size < slova[el]:
            max_size = slova[el]
            answer = []
        if max_size == slova[el]:
            answer.append(el)
    return sorted(answer)[0]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        text = f.read()
    res = main(text)
    print(res)

    assert main("apple orange banana banana orange") == "banana"
    assert main("oh you touch my tralala mmm my ding ding dong") == "ding"
    assert main('''q w e r t y u i o p
a s d f g h j k l
z x c v b n m''') == "a"
    assert main("1 0 0 0 0 0 1 1 1 1") == "0"
    assert main("0") == "0"
    assert main("a c") == "a"
