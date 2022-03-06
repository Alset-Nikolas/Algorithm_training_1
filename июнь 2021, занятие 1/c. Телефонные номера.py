def format_tel(tel):
    tel = ''.join(tel.split("-"))
    tel = ''.join(tel.split("("))
    tel = ''.join(tel.split(")"))
    if len(tel) == 7:
        tel = '8495' + tel
    if tel.startswith("+7"):
        tel = '8' + tel[2:]
    return tel


def proverka(tel1, tel2):
    if tel1 == tel2:
        return 'YES'
    return "NO"


find_tel = format_tel(input())
for i in range(3):
    over_tel = format_tel(input())
    res = proverka(find_tel, over_tel)
    print(res)
