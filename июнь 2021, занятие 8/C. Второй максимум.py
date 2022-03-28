class BineryElement:
    def __init__(self, value):
        self.value = value
        self.right_person = None
        self.left_person = None
        self.depth = None
        self.parent = None

    def __str__(self):
        return f" {self.value}\n\tL={self.left_person}\n\tR={self.right_person} "


class BinerTree:
    flag_print = True

    def __init__(self, val):
        self.root = BineryElement(val)
        self.value = self.root.value
        self.depth = 1

    def add_number(self, val):
        parent_tree = self.root
        h = 1
        while parent_tree is not None:
            if parent_tree.value == val:
                break
            h += 1
            if h > self.depth:
                self.depth = h
            if val < parent_tree.value:
                left_tree = parent_tree.left_person
                if left_tree is None:
                    new_el = parent_tree.left_person = BineryElement(val)
                    new_el.depth = h
                    new_el.parent = parent_tree
                    break
                parent_tree = parent_tree.left_person
            elif val > parent_tree.value:
                right_tree = parent_tree.right_person
                if right_tree is None:
                    new_el = parent_tree.right_person = BineryElement(val)
                    new_el.depth = h
                    new_el.parent = parent_tree
                    break
                parent_tree = parent_tree.right_person

    def __str__(self):
        return str(self.root)


def go_right(tree):
    if tree.right_person is not None:
        return go_right(tree.right_person)
    return tree


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    BT = BinerTree(numbers[0])
    for i, val in enumerate(numbers[1:-1]):
        BT.add_number(val)
    max_binary_element = go_right(BT.root)
    if max_binary_element.left_person is None and max_binary_element.right_person is None:
        val = max_binary_element.parent.value
    else:
        val_element = go_right(max_binary_element.left_person)
        val = val_element.value
    print(val)
