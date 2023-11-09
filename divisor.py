def divisor(a):
    b = 0
    for i in range (1,1+a):
        if a % i == 0:
            b += 1
    return b 
Max_Count = 0
for j in range(5):
    Num = int(input())
    Count_divisor = divisor(Num)
    if Count_divisor > Max_Count:
        Max_Count = Count_divisor
print(Num , Max_Count)

        
    