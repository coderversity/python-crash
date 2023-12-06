def debug(tag, outputVal):
    print(f'{tag}: {outputVal}')


# Variables and Data Types
x = 5
y = 2.5
name = "Alice"
is_student = True

# Basic operations
sum = x + y
debug('sum', sum)

diff = x -y
debug('difference', diff)

product = x * y
debug('product', product)

quotient = x / y
debug('quotient', quotient)

remainder = 13 % 5
debug('remainder (moulus)', remainder)

# type casting - decimal to int
quotient_as_int = int(quotient)
debug('casted to int', quotient_as_int)

# type casting - boolean to string
is_student_as_str = str(is_student)
debug('casted to string', is_student_as_str)
debug('check type', type(is_student_as_str))

""" Control structures """
# If statement
age = 20

if age >= 18:
    print('You are an adult.')
elif age > 65:
    print('You are a senior citizen.')
else:
    print('You are a minor.')

# using and/or
is_sunny = True
is_weekend = False

if is_sunny and is_weekend:
    print("Let's go outside!")
elif is_sunny or is_weekend:
    print("No work to do today!")
else:
    print("I have to work today.")


# Comparison operators
x = 10
y = 5

if x > y:
    print(f'{x} is greater than {y}')
elif x < y:
    print(f'{x} is less than {y}')
else:
    print('x is equal to y')

z = 5

is_greater_than_or_equal = z >= 5
debug('greater than or equal', is_greater_than_or_equal)

is_less_than_or_equal = z <= 5
debug('less than or equal', is_less_than_or_equal)

is_not_equal = z != 5
debug('not equal', is_not_equal)

# inverse boolean
is_stuent = True
debug('Inverse of is_student', not is_student)

""" DATA STRUCTURES """

# Lists are ordered and can contain duplicates. Their contents can be changed
my_list = [1, 2, 3, 4, 5]
debug('First item in list', my_list[0])  # Accessing elements

my_list.append(6)  # Adding elements
debug('entire list', my_list)

# remove duplicates from a list
my_list.append(1)
debug('list with dupe', my_list)

unique_list = list(set(my_list))
debug('unique list', unique_list)

# Tuples are ordered and can contain duplicates. They are immutable which means you cannot change their contents.
my_tuple = (1, 2, 3, 1, 3)

# remove duplicates from a tuple
unique_tuple = tuple(set(my_tuple))
debug('unique tuple', unique_tuple)

# Dictionaries
my_dict = {'name': 'Alice', 'age': 25}
debug('name', my_dict['name'])

# add entry to dictionary
my_dict['country'] = 'United States'
debug('country', my_dict['country'])

""" LOOPS """
# For loop
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    debug('for loop', number)

# While loop
count = 0

while count < 5:
    debug('while loop', count)
    count += 1

""" FUNCTIONS AND MODULES """

# Function with no parameter
def say_hello():
    print('Hello World!')

say_hello()

# Function with parameters
def greet(time_of_day, name):
    print(f'Good {time_of_day.capitalize()} {name}!')

greet('morning', 'John')
greet('evening', 'Jane')

# modules and packages can be imported
import math
debug('Square root', math.sqrt(25))

""" CLASSES """
# Create class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print('Woof woof!')

my_dog = Dog('Buddy', 3)
debug('dog name', my_dog.name)
my_dog.bark()

""" FILE HANDLING """
filename = 'example.txt'

# writing to a file
file = open(filename, 'w')
file.write('This is a text file.')
file.close()

# reading entire contents from a file
with open(filename, 'r') as file:
    content = file.read()
    print(content)

# reading file line by line
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character

# appending to a file
with open(filename, 'a') as file:
    file.write("\nThis text is appended to the file.")

""" EXCEPTION HANDLING """

# handling exception that gets raised if a file does not exist
try:
    with open('file_does_not_exist.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

# handling divide by zero exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")