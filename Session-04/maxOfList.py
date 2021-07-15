import math
count = input('Please enter your count : ')
numbers = []
i = 1
if count.isdigit():
    num_count = int(count)
    while i<=num_count :
        in_str = input('Enter number {} : '.format(i))
        if in_str.isdigit():
            numbers.append (int(in_str))
            i += 1
        else :
            print('Please enter valid number')
    print('max number is {}'.format(max(numbers)))
else :
    print('Erro')

print('********************')
i = 1
res = numbers[0]
while i<len(numbers):
    if math.fabs(numbers[i]-50 )< math.fabs(res-50) :
        res = numbers[i]
    i+=1
print('nazdiktarin addad be 50 => {}'.format(res))