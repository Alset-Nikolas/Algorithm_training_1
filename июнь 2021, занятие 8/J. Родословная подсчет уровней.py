import sys


def calc_my_childs(person):
    if parents[person] is None or person in people_finished_calc:
        return
    if parents[person] not in people_finished_calc:
        calc_my_childs(parents[person])
        people_finished_calc.add(parents[person])
    val_parent = parents[person]
    answer[person] += answer[val_parent] + 1
    people_finished_calc.add(person)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    n = int(input())
    parents = dict()
    childs = dict()
    answer = dict()
    for i in range(n - 1):
        child, parent = input().split()
        if child not in answer:
            answer[child] = 0
        if parent not in answer:
            answer[parent] = 0

        if child not in parents:
            parents[child] = None
        if parent not in parents:
            parents[parent] = None
        if parent not in childs:
            childs[parent] = set()
        if child not in childs:
            childs[child] = set()

        answer[parent] = 0
        parents[child] = parent
        childs[parent].add(child)

    people_finished_calc = set()

    for parent in parents.keys():
        calc_my_childs(parent)

    for name, val in sorted(answer.items()):
        print(name, val)
