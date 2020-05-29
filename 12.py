'''
12. Write a Python program to convert list to list of dictionaries.
'''
l=[['Simran','B.tech',20],['Abhishek','B.Tech',22]]
z=[]
for i in l:
    d={}
    d['Name']=i[0]
    d['Degree']=i[1]
    d['Age']=i[2]
    z.append(d)
print(z)    
