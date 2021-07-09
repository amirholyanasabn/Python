my_list = [12, 25, 1, 65, 97, 85, 10, 22, 55]
max_number = max(my_list)
print('max number => ',max_number)
print('------------------------------------')
input_number = int(input('Please enter a number : '))
my_list.sort(reverse=True)
result = my_list[input_number-1]
print(result)
print('-------------------------------------')
print(my_list)
first_index = my_list[0]
last_index = my_list.pop(-1)
# print(first_index,last_index)
my_list.append(first_index)
my_list[0] = last_index
print(my_list)
