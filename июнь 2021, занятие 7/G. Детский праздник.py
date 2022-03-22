if __name__ == '__main__':
    m_bols, n_people = list(map(int, input().split()))
    events = []
    people_index = dict()
    for i in range(n_people):
        t_i, z_i, y_i = list(map(int, input().split()))
        people_index[i] = 0
        times = []
        for j in range(z_i):
            times.append((j + 1) * t_i)
        povtor = 1
        while len(times) < m_bols:
            j += 1
            while len(times) < m_bols and j < (povtor+1)*z_i:
                j += 1
                new_t = povtor * (z_i * t_i + y_i) + times[j % z_i]
                times.append(new_t)
            povtor += 1
        for t in times:
            events.append([t, i])


    events.sort()
    i = 0
    while m_bols >0:
        time, name_index = events[i]
        people_index[name_index] += 1
        i+=1
        m_bols -= 1
    print(time)
    for x in range(n_people):
        print(people_index[x], end=" ")


