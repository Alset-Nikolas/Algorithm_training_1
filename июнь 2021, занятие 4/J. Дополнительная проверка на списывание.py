def check_word(word, numbers):
    if numbers == "no" and word[0].isdigit():
        return False
    return not word.isdigit()


def check_key_words(register, key_words, word):
    '''Проверяем word - ключевое слово '''
    if register == "yes":
        return word in key_words
    return word.lower() in key_words


def main(register, numbers, text, key_words):
    answer = []
    order_symvol = []
    all_symvol = set()
    max_repeat = 0
    data_dict = dict()

    for word in text.split():
        if not check_key_words(register, key_words, word) and check_word(word, numbers):
            if word not in all_symvol:
                all_symvol.add(word)
                order_symvol.append(word)
            if word not in data_dict:
                data_dict[word] = 0
            data_dict[word] += 1
            if max_repeat < data_dict[word]:
                max_repeat = data_dict[word]
                answer = []
            if data_dict[word] == max_repeat:
                answer.append(word)
    for x in order_symvol:
        for ans in answer:
            if x == ans:
                return x


if __name__ == '__main__':
    key_words = set()
    text_list = []
    with open("input.txt", "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            if i == 0:
                n, register, numbers = line.split()
                n = int(n)
                continue
            if n > 0:
                if register == "no":
                    new_key_word = line.split()[0].lower()
                else:
                    new_key_word = line.split()[0]
                key_words.add(new_key_word)
                n -= 1
            else:
                res_line = []
                for x in line:
                    if not (x.isdigit() or x.isalpha() or x == "_" or x == " " or x == "\n"):
                        res_line.append(" ")
                    else:
                        if register == "no":
                            res_line.append(x.lower())
                        else:
                            res_line.append(x)
                text_list.append("".join(res_line))
    text = "".join(text_list)
    res = main(register, numbers, text, key_words)
    print(res)
