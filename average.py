Number = int(input("Enter Number:"))
Sum = 0
Count = 0
while Number !=  -1:
    Sum = Sum + Number
    Count = Count + 1
    Number = int(input("Enter Number:"))
Average = Sum / Count
print("The average   is equal to", Average)
