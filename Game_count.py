Count = int(input())
A = 0
Player =[]
for i in range(Count):
    Player_count = int(input())
    Player.append(Player_count)
Player.sort()
for j in range(0,Count):
    if (Player[j] <= 2):
        A += 1
print(A//3)
