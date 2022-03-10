def main(text, info):
    res = 0
    # knowname_words= dict()
    words = text.split()
    for word in words:
        word_lower = word.lower()
        if word_lower in info:
            flag_right = False
            for right_world in info[word_lower]:
                if right_world == word:
                    flag_right = True
                    break
            if not flag_right:
                res += 1
        else:
            # if word_lower not in knowname_words:
            start_ord = ord("A")
            end_ord = ord("Z")
            number_beats = 0
            for symvol in word:
                if start_ord <= ord(symvol) <= end_ord:
                    number_beats += 1
            if number_beats != 1:
                res += 1
            #     else:
            #         knowname_words[word_lower] = word
            # else:
            #     if knowname_words[word_lower] != word:
            #         res+=1
    return res


if __name__ == '__main__':
    n = int(input())
    info = dict()
    for i in range(n):
        new_word = input()
        new_word_lower = new_word.lower()
        if new_word_lower not in info:
            info[new_word_lower] = set()
        info[new_word_lower].add(new_word)
    text = input()
    res = main(text, info)
    print(res)

    assert main(text="thE pAge cAnnot be found", info={'cannot': {'cAnnot'}, 'found': {'fOund'}, 'page': {'pAge'}}) == 2
    assert main(text="The PAGE cannot be found", info={'cannot': {'cAnnot'}, 'found': {'fOund'}, 'page': {'pAge'}}) == 4
    assert main(text="th", info={}) == 1
    assert main(text="thE", info={'the': {'thE'}}) == 0
    assert main(text="thE", info={'the': {'tHe'}}) == 1
    assert main(text="thE thE", info={'the': {'tHe'}}) == 2
    assert main(text="A", info={}) == 0
    assert main(text="A A", info={}) == 0
