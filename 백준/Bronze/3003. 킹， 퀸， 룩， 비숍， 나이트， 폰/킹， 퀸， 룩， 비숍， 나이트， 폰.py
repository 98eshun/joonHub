li = list(map(int, input().split()))
s = [1, 1, 2, 2, 2, 8]

for i in range(len(s)):
    li[i] = s[i] - li[i]
    print(li[i])