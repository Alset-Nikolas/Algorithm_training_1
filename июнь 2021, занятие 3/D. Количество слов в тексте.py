def main(text):
    return len(set(text.split()))


if __name__ == '__main__':
    text = ''
    with open("input.txt", "r") as f:
        text = f.read()
    res = main(text)
    print(res)

    assert main('''She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.
''') == 19

