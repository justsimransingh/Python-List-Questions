'''
13. Write a Python program to sort a list of nested dictionaries
'''
l=[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
l.sort(key=lambda e: e['key']['subkey'],reverse=True)
print(l)
