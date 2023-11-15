string = "salam jadi halet chetore bishoor"
counter = dict()
for letter in string:
    if letter in counter:
        counter[letter] += 1
    else:
         counter[letter] = 1
counter.pop(" ")
for A in list(counter.keys()):
    print("harfe", A , counter[A],"baar tekrar shode ast.")
