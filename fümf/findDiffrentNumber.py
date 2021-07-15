numbers = [65,65,65,65,65,65,65,65,65,65,65,65,35]
numbers.sort()
temp = numbers[0]
if numbers.count(temp) == 1 :
     print(temp)
elif numbers.count(temp) > 1 :
    print(numbers[-1])
else :
    print('not found')