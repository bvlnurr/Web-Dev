N = int(input()) 
count = sum(1 for _ in range(N) if int(input()) == 0) 
print(count)  
