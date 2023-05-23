n = int(input())
li = list(map(int, input().split()))
li2 = list()
m = max(li)
all=0

for i in li:
    li2.append(i/m*100)

for i in li2:
    all += i

print(all/n)