T = int(input())
li=[]
for i in range(T):
    r, s = input().split()
    for j in s:
        li += j*int(r)
    li += "\n"
for i in li:
    print(i,end='')