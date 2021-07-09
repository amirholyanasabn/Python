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
w = [12, 22, 33, 44, 55]
# del w[:]
# del w
w.clear()
print(w)
names.reverse()
print(names)
new_names = names[::-1]
print(new_names)

a = [1, 2, 3]
b = a
b[0] = 12
print(b)
print(a)
min_a = min(a)
max_a = max(a)
print(min_a,max_a)
r = list(range(0,5))
print(r)
r = range(5)[-1]
print(r)