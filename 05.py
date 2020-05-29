'''
5. Write a Python program to split a list based on first character of word.
'''

l = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for i in l:
    print("'{}'".format(i[0]))
    for j in l:
        if j.startswith(i[0]):
            print(' ',j)
