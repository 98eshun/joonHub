T = int(input())

for i in range(T):
    result = 0
    temp = 0
    n = input()
    for j in n:
        if j == "O":
            temp += 1
            result += temp
        else:
            temp = 0
    print(result)