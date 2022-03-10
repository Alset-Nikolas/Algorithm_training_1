def main(text, info):
    res = 0
    knowname_words= dict()
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
            if word_lower not in knowname_words:
                start_ord = ord("A")
                end_ord = ord("Z")
                number_beats = 0
                for symvol in word:
                    if start_ord <= ord(symvol) <= end_ord:
                        number_beats += 1
                if number_beats != 1:
                    res += 1
                else:
                    knowname_words[word_lower] = word
            else:
                if knowname_words[word_lower] != word:
                    res+=1

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
    print(info)
    res = main(text, info)
    print(res)

    assert main(text="thE pAge cAnnot be found", info={'cannot': {'cAnnot'}, 'found': {'fOund'}, 'page': {'pAge'}}) == 2
    assert main(text="The PAGE cannot be found", info={'cannot': {'cAnnot'}, 'found': {'fOund'}, 'page': {'pAge'}}) == 4
    assert main(
        text="ciFqrfIxe LgvqquN zvdlhnXJ tizFPXtv JxqWqgnR CabaJ hFYoqbhH UyfiTXO YvAylvnc ymtHHfnqh"
             " bmTLsEnh hikroekt dtVSftFBz ofQrMfo jGTGofv dVRwfJw UaRfzE wbjjGsM xKcezhleq XskqyXtl"
             " pWCkyr JcuiiawHw hHBbOV pIfztqkuo PNbjXhtoi lvthZdUc oozdiZCq xDdnpRqsD HDfocjpl aziTbCh"
             " jsJMkTpaG voKfnjYb ADtpndbo gwOkCvJs hGnvtbM NkFodqOwy BOgxWv qzMsbelpO tlQnic QlxjhTzNj "
             "OZvzmoNX NlbLsjq OvkpysLzc BFCjEESh aiLyKJas zhJbcdu vqxrKhgke BsEikapC aCCoHAFR qNSYNouc"
             " TboUQd bOJWCAy NiNkHPmA wsGXhub xIvDhv qeGgpTBkd XPOkfsxz bbgcyuWq YHioAxh mngcZbpgh qgbfVztk"
             " JMusos ogpskgdN HUmedvmA GhhpYKH vduijcpv rfMZlB rvpodvq UogggJX yhnKvOpz cKQHazal xdXpPMCzn"
             " zaYdrbic FYDsrfaF kFpUcXtY jihQVZ nhpgJXoT rwJokNFH eGvoNulk LugdwQRbl xlRQdy mOrvmCmhG tJpEDolo "
             "zLhXCegyl Orrnefa sQqsjckkm BaadhPSXa vLmbthY mlwXEbpns oLctMjmM spQHUtA qnxUrLGo ScAndtRh apdwiTV "
             "odtrlufr zkrreoWHT wbOJLyIvn TDPtdjFp CJtnhbNr ohkLVpww vJLdOfp ctswuolD kuIdtiWLq pHQvvlN uzEgrQhpG "
             "ncHyqZzt gkntqtmx ZAvUjYgJ hbjSXnN URnTcdbRk wMdRlrQ ilpvgMpja oIjXxmG sdnIJTkk bFvhViK dpdtgpt CembyhyMM"
             " RcBIirR rWyYzJfc UNbTfQQ plxhCpee bUbkgdDF JTgQAQhvp onFayvlm rykjyldhw xAuEnxF phbhlXB xxDDxfSfM aPHXcXsag "
             "sTseOhrrY MMiaCH avfBbeIfl hrtuxe zJlubLs Wwwdjvc JBnqWcAl hDXOdeHZr Nelvhp ydmbzqym kzbCxuN rNQCDbeqB "
             "VRaax yykZbEzOc XomeWckS jBrCrHrx FzGrd YvfUzRryb YYPSRO wxBazrm EkezBXg aUiYcod aTtjEEpz WczSYbDx tlFeIKB "
             "LlSQDtyVa iMGfoQ WyXVU wakvcqSU loKOoSnzA pWywmptia RcEMjACB bfyrkwpLp iSofdn SacAoja uIkcgpWnM dkqErpG nkxTwHfh"
             " srejafR rjXxUCQ BCstjy LBdeArjn SbunWWcd FmTkfGwh nyGRjOi VlZjliwD lQhjguWx IkemfP VGfqFBuiN aYrbvKu iabtpq QnjzcKE"
             " sffhhZYY JuooLppkr LqyjiBC WySPUmsQb CXjftV TmtgreN cicNuaor YIgdgc vTFwiGktI TNFmWdHU DpfEtwtf zssykzEsf xcsCKfnaS "
             "OBEwUVkzg PgArpsz RmUcaQels JmJaqn IcXnrvhkg vgkOPzmv BezbGaMfb bnjTmLse TnkNLq CxfpAoD slhLtnoaP jnppioo STcoufpS XmRtQqd"
             " yDpbsld qrVIEXn VZhmozgvr zuELbtea WiOopcPg vRwLRoy TyJkPUvOq yZSsjoi AzlwLPf suwNmPrzF kuJeUivG EnTHwlj XpZkNZH xygjBcx"
             " bTytkWFW ygKis iwjgktgw DzFDkhb elWPfddxy TyvlSNVR OBqjNCtXI cSYxJTb DqedLuqN vxikfztEc AbcQgnxiS bdCmDnn VbLDUWsz eeuucmp"
             " osIYklu sLXmxRipG yswHjZayD bMihpnRs lmyVpf gtfkgpmbB buPjpqli yxFSIu Ggjzeqm dTqrvPtei XduXypxn BykKgHhqe ewcUDvM lxWoiXBT"
             " HeqhAZu ialinsqW lcNzJmK yCKPbQrz hOjxGWvPq HgenCiuw QnWaEtz lRvwixAj otnJuciJ qtNWZPtL tJYiHzUiG rNhaIjil Oggvgmdq nhylWth "
             "VhrHlcnJV ceHFAVnU udtpWoJ wiQAeN mUkmTUv BqnLMdeSy kiffoynx vsnzxZe QbyfijgM ecxxWebWo TFoLnXouN SldaeWjV fuXlPWzBg qNNShyw"
             " avvNUgmP lhblkew svZdutKT avlFkl Afntea NrGVToH Hlvkxnut NbNbQXnc ugqqBFWcq bphIBvYpz FuuAUB CnqFfWxy lNdVncXmk UBvozFuqz muVHqMpa"
             " vcyQgcXN lfzcMdN eMmz ehXopYXAg GjBapgXVY qimorSZZt YEyoXzclm eUlyvxi aFrOSW htxGkVuJ ydszmKyb zAvzlkXM oRQizsGBz gZodlbKg pwQSugvyq "
             "MOvfpsCs tGNJBf lZqEdtPD sHYmFjcH wkRltsoYz qkWmhhBJ wgATDnhc HnbkMwnRv oSolCjBj xyQfzgenj xBtaqrEj eoCCfSg xYgfXZ htSgaFlbt DPrfLUw bdhrUaqT"
             " IabsomJE cyVtEg SMntmDjx jwwkwJkRo HeFyGSaTh KiSTzh dBCcqt vnAunEzf kGzwbur qmkMBbGCw Tdkunrkh YrYVnrbC muJSHjn Unuwgjfj ObbZfLsWd UjmxpJN"
             " KNlbLhF jFlbrLf pyOglE", info={}) == 296

    assert main(text="th", info={}) == 1
    assert main(text="thE", info={'the': {'thE'}}) == 0
    assert main(text="thE", info={'the': {'tHe'}}) == 1
    assert main(text="thE thE", info={'the': {'tHe'}}) == 2
    assert main(text="A", info={}) == 0
    assert main(text="A A", info={}) == 0
