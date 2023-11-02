Number = int(input())
if Number % 10 == 0 :
    print (Number)
else: 
    Number = (((Number//10)+1)*10)
    print(Number)