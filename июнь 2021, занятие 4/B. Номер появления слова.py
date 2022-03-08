def main(text):
    info = dict()
    slova = text.split()
    answer = []
    for slovo in slova:
        if slovo not in info:
            info[slovo] = 0
        else:
            info[slovo] += 1
        answer.append(str(info[slovo]))

    return ' '.join(answer)

if __name__ == '__main__':
    text = ''
    with open("input.txt", "r") as f:
        text = f.read()
    res = main(text)
    print(res)

    assert main("one two one tho three") == '0 0 1 0 0'
    assert main('''She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.

''') == "0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0"
    assert main('aba aba; aba @?"') == "0 0 1 0"