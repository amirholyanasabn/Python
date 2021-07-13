input_number = (input('Please enter a number : '))
if (input_number.isdigit()) :
    input_number = int (input_number)
    if input_number <= 20 and input_number >=17:
        print("A")
    elif input_number<17 and input_number >= 15 :
        print("B")
    elif input_number < 15 and input_number >= 12 :
        print("C")
    else :
        print("D")
else :
    print("Not Valided number.....")

