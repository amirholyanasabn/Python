in_number = input('Please enter number : ')
res = 0
if in_number.isdigit():
    in_number = int(in_number)
    for num in range (1,in_number+1):
        print(res,num ,end=' ')
        res += num
else :
    print('Error')
print('Fibonachi {} is {} .'.format(in_number,res))

