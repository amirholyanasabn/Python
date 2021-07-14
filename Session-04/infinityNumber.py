res_list = []
in_string = input('Please enter number : ')
if in_string.isdigit():
    number = int(in_string)
    in_question = input('Do you want to continue ?')
    res_list.append(number)
    while in_question == 'y':
        number =int (input('Please enter number : '))
        res_list.append(number)
        in_question = input('Do you want to continue ?')
   
else :
    print ('bye')
res_list.sort()
print(res_list)