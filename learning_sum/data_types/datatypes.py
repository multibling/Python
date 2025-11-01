# What is data types
'''
str - "hello"

int - 10

bool - True

# Python automatically detect data types

# Dynamic: Data types can change anytime

# Data stored in different types and sizes
'''

# Data Types
'''
No value = none (nothing)

# Primative types
Single value = integer_50
            float_3.14
            string_"hello"
            bool_True

# Data structures or Collections containers
Multiple value = List_[1,2,3]
            dictionary_{"a":1, "b":2, "c":3}
            set_{1,2}
            tuple_('a', 'b', 'c')
'''

# integer: whole numbers without decimals
a = 10  # int

# Float: numbers with decimal point
b = 3.15    # Float

# String: represent text or a sequence of characters
# written inside single or double quotes
c = "Hello"  # str
d = 'Hi'
e = "1234"

# Bool: can be either True or False
# used to handle logic and decision-making
# case-sensitive: they must start with a capital letter
f = True    # bool
g = False

# None: means 'no value', "nothing" or "unknown"
# it's used to show the absence of any data
h = None    # NoneType

# Blank "" is a string value with no characters inside, it is not same as None!
i = ""      # str - blank

# Whitespace " " is a string value with 1 or more spaces,
# it is not same sa None!
j = " "     # str - Empty space


# Data Types, Functions and Methods
# --------------------------

# Functions and Data Types
'''
Do something = Functions
Data = value
'''

# Types of Functions
'''
Standalone functions - print()
                    - type()

Methods of class - upper()
                - replace()

Operations - Magic Methods (+ - < > == in or)

user defined - the ones user created on his own
'''

# Libraries
'''
Standard Library = comes with python3

3rd-party Libraries - Pandas
                    - Numpy
                    - TensorFlow
'''

'''
# Functions
Indipendent block of code

# Syntax
function_name(value)
'''
print('hello')
type(50)


'''
# Methods
Function belong to objects/classes

# Syntax
value.method_name()
'''
'hello'.upper()
# 50.bit_length() - values can also be used

text = 'hi'
number = 10

# type(): returns the data type of a value,
# so you know what kind of object it is.
print(type(text))
print(type(number))

# len(): gives the total count of items inside a value,
# helping you mature its length
print(len(text))
# print(len(number))      # cannot be done error

# upper(): Converts all letters in a string to uppercase
print(text.upper())
# print(number.upper())   # cannot be done error

# bit_length(): Returns the length of a number in binary
# print(text.bit_length())    # cannot be done error
print(number.bit_length())

# Challenge
age = 35
height = 1.79
name = "Bling"
student = True
no_value = None

print(age)
print(height)
print(name)
print(student)
print(no_value)
print("")
print(type(age))
print(type(height))
print(type(name))
print(type(student))
print(type(no_value))
print("")
# print(len(age))
# print(len(height))
print(len(name))
# print(len(student))
# print(len(no_value))
print("")
