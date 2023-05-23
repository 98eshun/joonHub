n = int(input())
count = 0
for i in range(n):
    li = []
    temp = True
    s = input()
    for j in range(len(s)):
        if s[j] in li and s[j] != s[j-1]:
            temp = False
            break
        else : li += s[j]

    if temp == True : count += 1

print(count)