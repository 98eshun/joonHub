li = list()
li2 = list()
for _ in range(10):
    T = int(input())%42
    li.append(T)

for i in li:
    if i not in li2:
        li2.append(i)

print(len(li2))