in_string = input('Please enter your number : ')
fact = 1
if in_string.isdigit():
    in_num = int(in_string)
    for val in range(in_num,0,-1):
        fact = fact * val
else :
    print('Invalid input')
print(fact)