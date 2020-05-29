'''
6. Write a Python program to find missing and additional values in two lists.
Sample data : Missing values in second list: a,b,c
Additional values in second list: g,h
'''

l=['a','b','c','d','e','f']
z=['d','e','f','g','h']
missing = list(filter(lambda x:x in l and x not in z,l))
additional = list(filter(lambda x:x not in l and x in z,z))
print('Missing values=',missing)
print('Additional values=',additional)
