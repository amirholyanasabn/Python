in_number = input('Please enter your number : ')
res = 1
if in_number.isdigit():
    in_number = int(in_number)
    for num in range(1 , in_number+1):
        res = res * num
else :
    print('Error')
print('Factorial {} is {} .'.format(in_number,res))