n = map(int, input().split())
result = 0

for i in n:
    i *= i
    result += i
result = result % 10
print(result)