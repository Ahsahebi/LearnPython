word = input()
if ("AB" in word):
    B = word.find("B")
    word = word[B+1:]
    if ("AB" in word) or ("BA" in word):
        print ("YES")
    else:
        print("NO")
elif ("BA" in word):
    A = word.find("A")
    word = word[A+1:]
    if ("AB" in word) or ("BA" in word):
        print ("YES")
    else:
        print("NO")
else:
    print("NO")
