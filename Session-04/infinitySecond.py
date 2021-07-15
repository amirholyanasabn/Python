numbers = []
main_flag = True
while main_flag is True :
    in_string = input('Enter number : ')
    numbers.append(float(in_string))
    second_flag = False
    while second_flag is False :
        temp = input('Do you want to continue(y/n) ? ')
        if temp == 'n':
            second_flag = True
            main_flag = False
        elif temp == 'y':
            second_flag =True
            main_flag =True
        else :
            print('Only answer y or n ...')
numbers.sort()
print('list of number {} '.format(numbers))    
