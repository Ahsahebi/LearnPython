Number = int(input())
Name_total =[]
vote_counting =dict()
for i in range(Number):
    Name = input()
    Name_total.append(Name)
for j in Name_total:
    if j in vote_counting.keys():
        vote_counting[j] += 1
    else:
        vote_counting[j] = 1
Name_list = list(vote_counting.keys())
Name_list.sort()
for k in Name_list:
    print(k ,vote_counting[k])
