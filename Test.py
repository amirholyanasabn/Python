# first_name = input('Please enter your name : ')
# print(first_name+" Olyanasab")
m = [1, 5, 8, 9, 21, 47, 54, 11]
print(len(m))

m.append('Amirhossein')
print(m)
m.append([12, 22, 33])
print(m)
print(m[-1])
m[len(m):] = [65]
print(m)
# print(type (m[len(m):]))
m.append(12)
print(m)
n = [12, 22, 32, 42, 52]
print(n)
print('---------')
n[len(n):] = [62, 72, 82, 92]
print(n)
n[len(n)-2:] = [1, 2, 3]
print(n) 
n[1:3] = []
print(n) 
n.append(['amir','gucci'])
print(n)
n = n[:len(n)-1]
print(n)
n.extend(['amir,gucci'])
print(n)
n = n[:len(n)-1]
print(n)
n.extend([10, 20, 30])
print(n)
n.extend([12, 22, [55, 66], 'Sepideh', 66])
print(n)