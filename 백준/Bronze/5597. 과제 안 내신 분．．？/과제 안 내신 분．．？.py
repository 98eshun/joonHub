li = [i+1 for i in range(30)]
li2 = list()

for _ in range(28):
    n = int(input())
    li.remove(n)

for q in li:
    print(q)
