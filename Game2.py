import random
Happened = random.randint(1,100)
print(Happened)
Answer = input()
while Answer != "d":
    if Answer == "k":
        Happened = random.randint(1,Happened)
        print(Happened)
    elif Answer == "b":
        Happened = random.randint(Happened,100)
        print(Happened)
    Answer = input()
print ("oh yes! Adade morde nazare man ", Happened , " bood")