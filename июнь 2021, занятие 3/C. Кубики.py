def cubes(n_cubes, m_cubes):
    n_cubes = set(n_cubes)
    m_cubes = set(m_cubes)
    n_and_m = n_cubes & m_cubes
    n_dif = n_cubes - n_and_m
    m_dif = m_cubes - n_and_m
    all = [n_and_m, n_dif, m_dif]
    answer = []
    for set_ in all:
        res_items = sorted(list(set_))
        answer.append([len(set_), res_items])
    return answer

def pprint(res):
    for len_set, res_items in res:
        print(len_set)
        for x in res_items:
            print(x, end=' ')

        print()

def main():
    N, M = list(map(int,input().split()))
    n_cubes = []
    m_cubes = []
    for x in range(N):
        n_cubes.append(int(input()))
    for y in range(M):
        m_cubes.append(int(input()))
    res = cubes(n_cubes, m_cubes)
    pprint(res)


if __name__ == '__main__':
    main()

    assert cubes([0, 1, 10, 9], [1, 3, 0]) == [[2, [0, 1]], [2, [9, 10]], [1, [3]]]
    assert cubes([1, 2], [2, 3]) == [[1, [2]], [1, [1]], [1, [3]]]
    assert cubes([], []) == [[0, []], [0, []], [0, []]]
