def main(gen1, gen2):
    base_gen_1 = dict()
    base_gen_2 = dict()
    for i in range(len(gen2)-1):
        el = gen2[i]+gen2[i+1]
        if el not in base_gen_2:
            base_gen_2[el] = 0
        base_gen_2[el] +=1
    for i in range(len(gen1)-1):
        el = gen1[i]+gen1[i+1]
        if el not in base_gen_1:
            base_gen_1[el] = 0
        base_gen_1[el] +=1
    res = 0
    for key, val in base_gen_1.items():
        if key in base_gen_2:
            res += val
    return res


if __name__ == '__main__':
    gen1 = input()
    gen2 = input()
    res = main(gen1, gen2)
    print(res)

    assert main("ABBACAB", "BCABB") == 4
    assert main("A", "B") == 0
    assert main("A", "A") == 0
    assert main("AA", "AA") == 1
    assert main("AAA", "AAA") == 4
    assert main("AAA", "AAAA") == 6
    assert main('CBABB', 'CBBBA') == 4
    assert main('WIVYKHBSZLOGOROTIPKLQJWUVXLEZPAGPCDUPUZIDRJTMSHVDUEALKOILER', 'HYAASSTKFMSSTLQENNEIDYDMTTQPJHOYMYFLTCRQTARJHGFILQYENKPRCQHMEUZKQFZTXJFDBIMJJEKWMHFLKZBCUCCKYSGLVZ') == 7

    # test_list = ["A", "B", "C", "D"]
    # while 1:
    #     el1 = "".join([random.choice(test_list) for x in range(5)])
    #     el2 = "".join([random.choice(test_list) for x in range(5)])
    #     if main2(el1, el2) != main(el1, el2):
    #         print(el1, el2, main2(el1, el2), main(el1, el2))
    #         break