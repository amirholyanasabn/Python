a = [1, 6, 9, 12, 8]
b = [10, 20]
b.extend(a[2:])
print(b)
# a[2:] = a.extend(b)
a[2 : ] = b
print(a)