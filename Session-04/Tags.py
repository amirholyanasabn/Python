input_number = input('Please enter a number : ')
if  input_number.isdigit() != True:
    numbers = input_number.split('.')
    input_number = numbers[0]
if (int(input_number)) >= 1 and (int(input_number))<=7 :
    if(int(input_number)) == 1 :
        print('Montag')
    elif (int(input_number)) == 2 :
        print('Dienstag')
    elif (int(input_number)) == 3 :
        print('Mittwoch')
    elif (int(input_number)) == 4 :
        print('Donnerstag')
    elif (int(input_number)) == 5 :
        print('Freitag')
    elif (int(input_number)) == 6 :
        print('Samstag')
    else :
        print('Sonntag')
else :
    print('Wrong input ....')