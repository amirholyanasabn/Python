in_string = input('Please enter your number : ')
weak = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
if in_string.isdigit():
    in_number = int(in_string)
    if in_number>=1 and in_number<=7 :
        print(weak[in_number-1])
    else :
        print('Out of range')
elif '.' in in_string:
    in_split = in_string.split('.',1)
    if in_split[0].isdigit() and in_split[1].isdigit():
        in_number = int(in_split[0])
        if in_number>=1 and in_number<=7:
            print(weak[in_number-1])
        else:
            print('out of range')
    else :
        print('Error')
else :
    print('Invalid Information and try aganis...')