import random
magic_list = list(range(1,6))
magic_number = random.choice(magic_list)
print(magic_number)
in_string = input('Please enter your number : ')
if in_string.isdigit():
    in_number = int(in_string)
    while in_number != magic_number :
        in_number = int(input('Please enter your number : '))
        in_number == magic_number 
    else :
        print('Horaaaaa')   
else :
    print('Not valid')        