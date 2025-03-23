def power(a, n):
    return a ** n  

a, n = map(float, input().split())
n = int(n)  
print(power(a, n))
