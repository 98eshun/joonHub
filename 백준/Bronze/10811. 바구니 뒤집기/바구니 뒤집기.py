n, m = map(int, input().split())
li = [i+1 for i in range(n)]


for _ in range(m):
    i, j = map(int, input().split())
    x = (j-i+1) // 2

    for a in range(x):
        li[i+a-1], li[j-a-1] = li[j-a-1], li[i+a-1]

for i in li:
    print(i)