def divisor(a):
    b = 0
    for i in range(1, 1+a):
        if a % i == 0 :
            b += 1
    return b
Count_max= 0
for j in range (20):
    Num = int(input())
    Count_divisor = divisor(Num)
    if Count_divisor > Count_max:
        Count_max = Count_divisor
print (Num , Count_max)
    