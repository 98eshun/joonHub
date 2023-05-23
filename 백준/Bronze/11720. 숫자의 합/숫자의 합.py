n = int(input())
a = int(input())
b = 0

for i in range(len(str(a))):
    b += int(str(a)[i])

print(b)