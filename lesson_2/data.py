import math

first = "Philip"
last = "Davis"

# print(type(last))
# print(type(first)==str)
# print(isinstance(first, str))

# Constructor Function

# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza, str))

# concatenation 

fullname = first + ' ' + last
print(fullname)
fullname += " is cool!"
print(fullname)

year = str(1983)
print(type(year))
print(year)

year_born = "I was born in " + year + '.'
print(year_born)

# Multiple Line Statements
multiline = '''
Hey, how are you feeling?                                                 

I was just checking in.    
                            All good?

'''
# print(multiline)

# Escaping special characters
sentence = 'I\'m at work.\tHey!\n\n'
# print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(last.replace("Davis", "Butthead"))
print(len(multiline))
multiline += "                          "
multiline = "                          " + multiline 
print(len(multiline))

print(len(multiline.strip()))
print("")

# Build a menu
title = "menu".upper()
print(title.center(20, '='))
print('Coffee'.ljust(16,'.') + '$1'.rjust(4))
print('Tea'.ljust(16,'.') + '$2'.rjust(4))
print('Cake'.ljust(16,'.') + '$3.50'.rjust(7))
print('Scone'.ljust(16,'.') + '$2.50'.rjust(7))

# Some methods that return boolean data
print(first.startswith("P"))
print(last.endswith("s"))

# boolean data types
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# numeric data types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, bool))

# float type
gpa = 3.18
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for Numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))

# import the math module
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

