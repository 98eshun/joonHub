s = input().upper()
li = list(set(s))
a = []

for i in li:
    a.append(s.count(i))

if a.count(max(a)) >=2:
    print("?")
else:
    print(li[a.index(max(a))])