'''
8. Write a Python program to generate groups of five consecutive numbers in a list
'''

l=[1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
for i in range(0,len(l),5):
    print(l[i:i+5])
