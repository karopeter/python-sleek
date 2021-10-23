print("Karo Asakpa")
print('o----')
print(' ||||')
print('*' * 10)
price = 10
rating = 4.9
name = 'Choice'
is_published = False
print(price)
# A new patient was adimited to the hospital his name is John Smith and he's 20 years old is he
# new patient or an existing one
full_name = 'John Smith'
age = 20
is_new = True

# Getting and recieving input from user
name = input('What is your name? ')
print('Hi ' + name)

# Ask two questions: person's name and favorite color.
# Then, print a message like "karo likes blue"
name = input('What is your name? ')
favorite_color = input('What is your favorite color? ')
print(name + ' likes ' + favorite_color)

# Type Conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

# Ask a user their weight (in pounds), convert it 
# to kilograms and print it on the terminal
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

# Python strings
#course = "Python's Course for Beginners"
#another = course[:]
#print(another)
# print(course[0])
# print(course[-2])
# print(course[0:3])

# String methods
course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
#print(len(course))

# tripple quote strings
message = ''' 
 Hi John ,
 
 Here is our first email to you.
 
 Thank you,
 The support team
'''
print(message)

# Formatted Strings
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)

# Arithmetic operation
print (10 ** 3)
x = 10
x = x + 3
print(x)

# operator precedence
x = 10 + 3 * 2 ** 2
print(x)

x = (2 + 3) * 10 - 3
print(x)

# Math function
x = 2.9
print(round(x))

import math

#print(math.ceil(2.9))
print(math.floor(2.9))
x = 2.9
print(abs(-2.9))