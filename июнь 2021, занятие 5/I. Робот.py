def main(k, text):
    res = 0
    for i in range(len(text) - k):
        word = text[i:i + k]
        j = 0
        variant = 1
        while i + k * variant + j < len(text) and word[j] == text[i + k * variant + j]:
            res += 1
            j += 1
            if j >= k:
                j = j % k
                variant += 1
    return res


if __name__ == '__main__':
    k = int(input())
    text = input()
    res = main(k, text)
    print(res)

    assert main(2, "zabacabab") == 5
    assert main(2, "abc") == 0
