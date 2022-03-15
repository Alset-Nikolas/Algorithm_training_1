def main(k, text):
    res = 0
    len_povtor = 0
    for i in range(len(text) - k + 1):
        if i < len(text) - k and text[i] == text[i+k]:
            len_povtor += 1
        else:
            res += len_povtor * (len_povtor + 1) / 2
            len_povtor = 0
    return int(res)


if __name__ == '__main__':
    k = int(input())
    text = input()
    res = main(k, text)
    print(res)
    assert main(2, "zabacabab") == 5
    assert main(2, "abc") == 0
