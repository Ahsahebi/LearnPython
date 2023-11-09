Score = int(input())
count = 0
Total_score = 0
for i in range(4):
    if Score == 3:
        count += 1
    Total_score += Score
    Score = int(input())
print(Total_score,count)