students = []
    
for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
second_lowest = sorted(set(score for _, score in students))[1]
 
result = sorted([name for name, score in students if score == second_lowest])
    
for name in result:
        print(name)