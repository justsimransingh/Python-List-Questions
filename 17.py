'''
17. Write a Python program to iterate over two lists simultaneously.
'''
l=[1,2,3]
m=['a','b','c']
for a,b in zip(l,m):
    print(a,b)
