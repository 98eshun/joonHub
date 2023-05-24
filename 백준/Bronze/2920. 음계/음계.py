li = list(map(int, input().split()))
a = sorted(li)
b=[]
for i in reversed(a):
    b.append(i)

if li == a:
    print("ascending")
elif li == b:
    print("descending")
else:
    print("mixed")