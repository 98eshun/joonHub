a, b = map(int, input().split())

def change(i):
    a = i//100
    b = (i%100)//10
    c = i%10
    return c*100 + b*10 + a

ac = change(a)
bc = change(b)

if ac > bc : print(ac)
else : print(bc)