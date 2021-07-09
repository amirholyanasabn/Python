input_number = input('Please enter number : ')
number_list =  input_number.split(',')
print(number_list)
number_list.sort()
number_list.sort(key=len)
print(number_list)
count_nine = number_list.index('9')
count_nintyNine = number_list.index('99')
yekan = number_list[:count_nine+1]
print(yekan)
yekan_count = len(yekan)
dahgan = number_list[count_nine+1:count_nintyNine+1]
print(dahgan)
dahgan_count = len(dahgan)
sadgan = number_list[count_nintyNine+1:]
sadgan_len = len(sadgan)
print(sadgan)
print(yekan_count,dahgan_count,sadgan_len)