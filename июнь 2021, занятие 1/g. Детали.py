n, k, m = map(int, input().split())
if k < m or k > n:
    print(0)
else:
    details = 0
    balance = 0
    new_details = 0
    while n >= k:
        q_blanks = n // k
        mass_blanks = q_blanks * k
        balance += n - mass_blanks
        q_details = k // m * q_blanks
        new_details += q_details
        mass_details = q_details * m
        balance += q_blanks * k - mass_details
        n = balance
        balance = 0
    print(new_details)
