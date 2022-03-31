import sys


def calc_my_childs(person):
    if childs[person] == set() or person in people_finished_calc:
        return
    for child in childs[person]:
        if child in people_finished_calc:
            answer[person] += answer[child] + 1
        else:
            calc_my_childs(child)
            people_finished_calc.add(child)
            answer[person] += answer[child] + 1
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

    people_calc = set(x[0] for x in filter(lambda x: x[1] == set(), childs.items()))
    people_finished_calc = people_calc.copy()

    for parent in parents.keys():
        calc_my_childs(parent)

    for name, val in sorted(answer.items()):
        print(name, val)
