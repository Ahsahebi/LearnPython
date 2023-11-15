Number = int(input())
Name_total = ""
for i in range(Number):
    Name = input()
    Name_total += Name + " "
for word in Name_total:
    Name_total.find(word)
print(Name_total)
