import sys


def add_person(name):
    parent = child_parents[name]
    while parent != "":
        answer[parent] += 1
        parent = child_parents[parent]


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    n = int(input())
    parent_child = dict()
    child_parents = dict()
    answer = dict()
    for i in range(n - 1):
        child, parent = input().split()
        answer[child] = 0
        answer[parent] = 0
        if child not in child_parents:
            child_parents[child] = ""
        if child not in parent_child:
            parent_child[child] = set()
        if parent not in parent_child:
            parent_child[parent] = set()
        if parent not in child_parents:
            child_parents[parent] = ""
        child_parents[child] = parent
        parent_child[parent].add(child)

    for name in parent_child.keys():
        add_person(name)

    for name, val in sorted(answer.items()):
        print(name, val)

'''9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I'''
