Count = int(input())
Laptop = []
A = []
B = []
for i in range(Count):
    price_quality = input().split()
    Laptop = Laptop + price_quality
for j in range(0,Count):
    A.append(int(Laptop[j*2]))
    B.append(int(Laptop[j*2+1]))
for k in range(0,Count):
    if A[k] == min(A):
        if B[k] == max(B):
            print("happy irsa")
        else:
            print("poor irsa")
