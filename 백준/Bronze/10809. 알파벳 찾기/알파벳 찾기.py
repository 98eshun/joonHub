s = input()
li = [-1]*26

for i in range(len(s)):
    if li[ord(s[i])-97] == -1 : li[ord(s[i])-97] = i

for a in li:
    print(a)