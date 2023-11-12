Word = input()
Word_small = Word.lower()
count = 0
for i in range(0,len(Word)):
    if Word[i] == Word_small[i]:
        count += 1
if count >= (len(Word)/2):
    print (Word_small)
else:
    print(Word.upper())
