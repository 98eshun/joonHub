a = 0
b = 0
for i in range(20):
    li = list(input().split())
    li[1] = float(li[1])
    if "P" in li[2]:
        continue
    temp = 0.0
    if "A" in li[2]:
        temp += 4.0
    elif "B" in li[2]:
        temp += 3.0
    elif "C" in li[2]:
        temp += 2.0
    elif "D" in li[2]:
        temp += 1.0
    elif "F" in li[2]:
        temp += 0.0
    else:
        continue

    if "+" in li[2]:
        temp += 0.5

    a += li[1] * temp
    b += li[1]

if a != 0 :
    a = a/b
else:
    a = 0

print(f'{a : .6f}')