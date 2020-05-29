'''
19. Write a Python program to remove duplicates from a list of lists
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''

l=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
m=[]
for i in l:
    if i not in m:
        m.append(i)
m.sort()
print(m)        
