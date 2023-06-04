A = int(input())
B = int(input())
C = int(input())
x = A*B*C
y = str(x)

for i in range(10):
    print(y.count(str(i)))