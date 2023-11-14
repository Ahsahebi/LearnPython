Count = int(input())
Player =[]
for i in range(Count):
    Player_count = int(input())
    Player.append(Player_count)
Player.sort()
for j in range(0,Count):
    if (Player[j] > 2):
        Player.remove(Player[j])
print(len(player)//3)
