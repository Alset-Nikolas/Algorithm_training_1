def main(synonyms, slovo):
    return synonyms[slovo]

if __name__ == '__main__':
    n = int(input())
    synonyms = dict()
    for i in range(n):
        synonym1, synonym2 = input().split()
        synonyms[synonym1] = synonym2
        synonyms[synonym2] = synonym1
    slovo = input()
    res = main(synonyms, slovo)
    print(res)

    assert main({'Hello': 'Hi', 'Hi': 'Hello', 'Bye': 'Goodbye', 'Goodbye': 'Bye', 'List': 'Array', 'Array': 'List'}, "Goodbye") == 'Bye'
    assert main({'beep': 'Car', 'Car': 'beep'}, "Car") == "beep"
    assert main({'Ololo': 'Ololo', 'Numbers': '1234567890', '1234567890': 'Numbers'}, 'Numbers') == "1234567890"
