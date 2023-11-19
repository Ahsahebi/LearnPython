imprt math
Count = int(input())
number_total=[]
for i in range(Count):
    number = int(input())
    number_total.append(number)
for j in number_total:
    print(math.sqrt(j))
