Age = int(input())
Max_age = 0
while Age != -1:
    if Age > Max_age:
        Max_age = Age
    Age = int(input())
print(Max_age)