import random
magic_list =  list(range(1,101))
magic_number = random.choice(magic_list)
# magic_number = 50
hads = False
while hads is False :
    in_number = input('Enter number : ')
    if in_number.isdigit():
        num_int = int(in_number)
        if magic_number == num_int :
            print('bordi')
            hads = True
        elif magic_number > num_int :
            print('adade bozorgtar bego')
        else :
            print('adade kochektar bego')
    else :
        print('not valid')

