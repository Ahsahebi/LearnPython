import random
Answer = random.randint(1,100)
Happened = int(input("What is your happened? "))
while Happened != Answer:
    if Happened > Answer:
        print("mine is smaller")
    else:
        print("mine is larger")
    Happened = int(input("What is your happened? "))
print("Oh yes, the answer was equal to: " , Answer)