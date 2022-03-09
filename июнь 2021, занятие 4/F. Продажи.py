def main(text):
    bd_info = dict()
    for line in text.split("\n"):
        if len(line.split()) == 3:
            name, tovar, kol_vo = line.split()
            if name not in bd_info:
                bd_info[name] = dict()
            if tovar not in bd_info[name]:
                bd_info[name][tovar] = 0
            bd_info[name][tovar] += int(kol_vo)
    names = bd_info.keys()
    for name in sorted(names):
        print(f"{name}:")
        for items_ in sorted(bd_info[name].keys()):
            print(f"{items_} {bd_info[name][items_]}")

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        text = f.read()
    res = main(text)
