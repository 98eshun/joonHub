C = int(input())

result = []
for _ in range(C):
    sum = 0
    li = list(map(int, input().split()))
    for j in li[1:]:
        sum += j
    avg = sum / li[0]

    count = 0
    for j in li[1:]:
        if avg < j:
            count += 1

    per = (count / li[0]) * 100
    result.append('%.3f' % per + "%")
for i in result:
    print(i)