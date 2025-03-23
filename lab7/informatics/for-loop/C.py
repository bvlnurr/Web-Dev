import math

a = int(input())
b = int(input())

for i in range(math.ceil(math.sqrt(a)), math.floor(math.sqrt(b)) + 1):
    print(i * i)
