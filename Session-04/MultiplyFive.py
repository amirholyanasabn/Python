numbers = list(range(5,101,5))
sum = 0
index = 0
# print(type (numbers[0]))
while index < len(numbers) :
    print(numbers[index])
    # sum+=numbers[index]
    sum += numbers[index]
    index = index+1
print(sum)