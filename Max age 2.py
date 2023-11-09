Age = int(input())
Age_list =[]
while Age != -1: 
    Age_list.append(Age)
    Age = int(input()) 
Age_list.sort()
print(Age_list[-1], Age_list[-2])