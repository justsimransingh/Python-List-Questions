'''
10. Write a Python program to insert an element before each element of a list.
'''
l=['Simran','Deeksha','Muskan']
l.insert(0,'OK')
for i in range(1,len(l),2):
    l.insert(i+1,'OK')
print(l)
    
