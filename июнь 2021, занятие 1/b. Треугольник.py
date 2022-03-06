a = int(input())
b = int(input())
c = int(input())
if a * b * c == 0 or a < 0 or b < 0 or c < 0:
    print("NO")
elif a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
