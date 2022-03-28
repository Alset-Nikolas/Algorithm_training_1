class BineryElement:
    def __init__(self, value):
        self.value = value
        self.right_person = None
        self.left_person = None
        self.depth = None
        self.parent = None

    def __str__(self):
        # return f" {self.value}\n\tL={self.left_person}\n\tR={self.right_person} "
        return f"{self.value}"


class BinerTree:
    def __init__(self, val):
        self.root = BineryElement(val)
        self.root.depth = 1
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


def find_depth(tree, depth=1, max_depth=None):
    max_depth = max_depth or [1]
    if tree.left_person is not None:
        find_depth(tree.left_person, depth + 1, max_depth)
    if tree.left_person is None and tree.right_person is None:
        max_depth[0] = max(depth, max_depth[0])
    if tree.right_person is not None:
        find_depth(tree.right_person, depth + 1, max_depth)
    return max_depth[0]


def check_avl(tree, flag=None):
    flag = flag or [True]
    if tree.left_person is not None:
        check_avl(tree.left_person, flag)
    if tree.left_person is not None and tree.right_person is not None:
        if abs(find_depth(tree.left_person) - find_depth(tree.right_person) ) > 1:
            flag[0] = False
    if tree.left_person is None and tree.right_person is not None:
        if abs(find_depth(tree.right_person) - 0) > 1:
            flag[0] = False
    if tree.right_person is None and tree.left_person is not None:
        if abs(find_depth(tree.left_person) - 0) > 1:
            flag[0] = False
    if tree.right_person is not None:
        check_avl(tree.right_person, flag)
    return flag[0]


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    BT = BinerTree(numbers[0])
    for i, val in enumerate(numbers[1:-1]):
        BT.add_number(val)
    if check_avl(BT.root):
        print("YES")
    else:
        print("NO")
