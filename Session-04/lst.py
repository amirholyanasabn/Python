in_str_number = input('Please enter number : [,] => ')
numbers = []
in_number = in_str_number.split(',')
i = 0
while i < len(in_number):
    numbers.append(int(in_number[i]))
    i+=1
in_number = input('enter new number : ')
if in_number.isdigit():
    in_number = int(in_number)
    count = numbers.count(in_number)
    if in_number in numbers :
        print('Tedadde {} ast'.format(count))
        i = 0
        start = 0
        while i < count :
            temp = numbers.index(in_number,start,len(numbers))
            print('{} omin index => {}'.format(i+1,temp))
            i+=1
            start = temp + 1
    else :
        print('nist')
    
else :
    print('invalid input')
