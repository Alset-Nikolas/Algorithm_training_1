time_go_1 = int(input())
time_go_2 = int(input())
q_1 = int(input())
q_2 = int(input())

T_MIN_1 = time_go_1*(q_1-1) + q_1
T_MAX_1 = time_go_1*(q_1+1) + q_1
T_MIN_2 = time_go_2*(q_2-1) + q_2
T_MAX_2 = time_go_2*(q_2+1) + q_2
end = min(T_MAX_1, T_MAX_2)
start = max(T_MIN_1, T_MIN_2)

if end >= start:
    print(start, end)
else:
    print(-1)