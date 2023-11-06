# A lambda function is a simple expression that returns a value
squared = lambda num : num * num
print(squared(2))

addTwo = lambda num : num + 2
print(addTwo(16))

sum = lambda  a, b : a + b

print(sum(7, 9))

#####################################

def functionBuilder(x):
    return lambda num : num + x

# 10 is the x parameter
addTen = functionBuilder(10) 

# 7 is the num variable in our lambda
print(addTen(7))

#####################################
# Higher order functions are functions that are built into other functions

numbers = [3, 7, 9, 13, 16, 20, 27]

# This map function will iterate over each number in our list and apply our lambda function to it
squared_nums = map(lambda num : num * num, numbers)
print(list(squared_nums))

# This lambda function will return a true or false. Either it is equal to 0 or it is not.
# The filter function here will return the odd numbers
odd_nums = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))

########################################

from functools import reduce

new_numbers = [1, 2, 3, 5, 7, 1]

total = reduce(lambda acc, curr : acc + curr, new_numbers)
print(total)

names = ["Bob", "Joe", "Tom", "Big Billy Big Balls"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(f"The character count is: {char_count}")