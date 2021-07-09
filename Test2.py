names = ['ali', 'reza', 'amirhossein', 'elnaz', 'arshia', 'amin']
names.insert(2,'sepideh')
print(names)
del names[-1]
print(names)
names.remove('elnaz')
print(names)
names.append('amirhossein')
print(names)
c = names.count('amirhossein')
print('count of amirhossein is => ',c)
print(names.index('amirhossein'))
print(names.index('amirhossein',2,5))