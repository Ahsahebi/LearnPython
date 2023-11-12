Word = input()
Word.lower()
count = 0
for i in range(0,len(Word)):
    if Word[i]==Word[-i]:
        count += 1
if count == round(len(Word)/2,0):
    print("palindrome")
else:
    print("not palindrome")
