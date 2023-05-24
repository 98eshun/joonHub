s = input()
li = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in li:
    s = s.replace(i, "e")
print(len(s))