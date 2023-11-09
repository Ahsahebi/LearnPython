Score = int(input())
Wins = 0
Total_score = 0
for i in range(29):
    if Score == 3:
        Wins += 1
    Total_score += Score
    Score = int(input())
print(Total_score,Wins)