class BineryElement:
    def __init__(self, value):
        self.value = value
        self.right_person = None
        self.left_person = None
        self.depth = None

    def __str__(self):
        return f" {self.value}\n\tL={self.left_person}\n\tR={self.right_person}"


class BinerTree:
    def __init__(self, val):
        self.root = BineryElement(val)
        self.val = self.root.value
        self.depth = 1

    def add_number(self, val):
        start = self.root
        h = 1
        while start is not None:
            if start.value == val:
                break
            h += 1
            if h > self.depth:
                self.depth = h
            if val < start.value:
                left_start = start.left_person
                if left_start is None:
                    start.left_person = BineryElement(val)
                    start.left_person.depth = h
                    print(h, end=' ')
                    break
                start = start.left_person
            elif val > start.value:
                right_tree = start.right_person
                if right_tree is None:
                    start.right_person = BineryElement(val)
                    start.right_person.depth = h
                    print(h, end=' ')
                    break
                start = start.right_person

    def __str__(self):
        return str(self.root)


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    BT = BinerTree(numbers[0])
    print(BT.depth, end=" ")
    for i, val in enumerate(numbers[1:-1]):
        BT.add_number(val)
