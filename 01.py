'''

1. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

'''

l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l1=[]
for i in l:
    l1.append(i[1])
l1.sort()
count=0
choice=1
l2=[]
while(choice):
    for i in l:
        if i[1] == l1[count]:
            l2.append(i)
            count+=1
            if count>=len(l):
                choice=0
                break
print(l2)
