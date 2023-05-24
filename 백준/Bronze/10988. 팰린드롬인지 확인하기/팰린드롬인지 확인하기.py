s = input()
a = ""
for i in reversed(s):
    a += i

if s == a:
    print(1)
else:
    print(0)