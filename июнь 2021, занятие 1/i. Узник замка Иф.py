A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

D, E = max(D, E), min(D, E)
A, B = max(A, B), min(A,B)
B, C = max(B, C), min(B,C)
A, B = max(A, B), min(A,B)

if B <= D and C <= E :
    print("YES")
else:
    print("NO")


