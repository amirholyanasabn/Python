a = [1, 6, 9, 12, 8]
b = [10, 20]
b.extend(a[2:])
print(b)
# a[2:] = a.extend(b)
a[2 : ] = b
print(a)
c = a.pop(2)
print(c)
print(a) 
a.pop()
print(a)
m = [1, 9, 62, 14, 69, 21, 4]
m.sort()
print(m)
names = ['Majid', 'Hasin', 'Madineh', 'Sepideh', 'Gucci', 'Jeff', 'Amirhossein', 'Manizheh']
names.sort(key=None,reverse=False )
print(names)
numbers = ['65', '874', '1', '62', '236', '12', '123']
numbers.sort()
print(numbers)
numbers.sort(key=len)
print(numbers)
