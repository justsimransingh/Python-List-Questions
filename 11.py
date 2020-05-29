'''
11. Write a Python program to print a nested lists (each list on a new line) using the print() function.
'''
l=[['Hello','Hi','Hey'], ['OK','Alright','Fine'], ['Bye','See you','Tata']]
'''
for i in l:
    for j in i:
        print(j,end=' ')
    print()
'''
for i,j,k in zip(l[0],l[1],l[2]):
    print(i,j,k)
