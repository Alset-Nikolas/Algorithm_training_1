def new_client(bank_info, name):
    bank_info[name] = 0


def is_client(bank_info, name):
    if name in bank_info:
        return True
    return False


def add_money(bank_info, name, summa):
    bank_info[name] += summa


def update_money(bank_info, name, procent):
    procent = int(procent)
    if bank_info[name] > 0:
        bank_info[name] = int(bank_info[name] * (1 + procent / 100))


def main(text):
    bank_info = dict()
    res = []
    for line in text.split('\n'):
        line_slova = line.split()
        if len(line_slova)>1:
            command, parametrs = line_slova[0], line_slova[1:]
            if command == "DEPOSIT":
                name, summa = parametrs
                summa = float(summa)
                if not is_client(bank_info, name):
                    new_client(bank_info, name)
                add_money(bank_info, name, summa)
            elif command == "WITHDRAW":
                name, summa = parametrs
                summa = float(summa)
                if not is_client(bank_info, name):
                    new_client(bank_info, name)
                add_money(bank_info, name, -summa)
            elif command == "BALANCE":
                name = parametrs[0]
                if name in bank_info:
                    ans = str(int(bank_info[name]))
                else:
                    ans = "ERROR"
                res.append(ans)
            elif command == "INCOME":
                p = parametrs[0]
                p = float(p)
                for name in bank_info.keys():
                    update_money(bank_info, name, p)
            elif command == "TRANSFER":
                name1, name2, summa = parametrs
                summa = float(summa)
                if not is_client(bank_info, name1):
                    new_client(bank_info, name1)
                if not is_client(bank_info, name2):
                    new_client(bank_info, name2)
                add_money(bank_info, name1, -summa)
                add_money(bank_info, name2, summa)
    return res

# Входной файл содержит последовательность операций. Возможны следующие операции:
# DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если у клиента нет счета,
# то счет создается. WITHDRAW name sum - снять сумму sum со счета клиента name.
# Если у клиента нет счета, то счет создается. BALANCE name -
# узнать остаток средств на счету клиента name. TRANSFER name1 name2 sum -
# перевести сумму sum со счета клиента name1 на счет клиента name2.
# Если у какого-либо клиента нет счета, то ему создается счет. INCOME p
# - начислить всем клиентам, у которых открыты счета, p% от суммы счета.
# Проценты начисляются только клиентам с положительным остатком на счету,
# если у клиента остаток отрицательный, то его счет не меняется.
# После начисления процентов сумма на счету остается целой,
# то есть начисляется только целое число денежных единиц. Дробная часть начисленных процентов отбрасывается.


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        text = f.read()
    res = main(text)
    for x in res:
        print(x)
    assert main('''DEPOSIT Ivanov 100
INCOME 5
BALANCE Ivanov
TRANSFER Ivanov Petrov 50
WITHDRAW Petrov 100
BALANCE Petrov
BALANCE Sidorov''') == ["105", "-50", "ERROR"]

    assert main('''BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 100
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 150
BALANCE Petrov
DEPOSIT Ivanov 10
DEPOSIT Petrov 15
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 46
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 14
BALANCE Ivanov
BALANCE Petrov''') == ["ERROR", "ERROR", "100", "ERROR", "150", "110", "165", "156", "165", "156", "179"]

    assert main('''BALANCE a
BALANCE b
DEPOSIT a 100
BALANCE a
BALANCE b
WITHDRAW a 20
BALANCE a
BALANCE b
WITHDRAW b 78
BALANCE a
BALANCE b
WITHDRAW a 784
BALANCE a
BALANCE b
DEPOSIT b 849
BALANCE a
BALANCE b''') == ["ERROR", "ERROR", "100", "ERROR", "80", "ERROR", "80", "-78", "-704", "-78", "-704", "771"]