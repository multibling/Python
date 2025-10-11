# modules always on top
import math  # provides mathematical helpers

# string data type

# literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
#
# # is the first type equals to string
# print(type(first) == str)
#
# # is the first variable an instance of string
# print(isinstance(first, str))


# constructor function
# pizza = str("pepperoni")
#
# print(type(pizza))
#
# # is the pizza type equals to string
# print(type(pizza) == str)
#
# # is the pizza variable an instance of string
# print(isinstance(pizza, str))


# Concatenation
fullname = first + " " + last

print(fullname)

# Takes the value of 'fullname' and add to it
fullname += "!"
print(fullname)


# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)


# Multiple lines
multiline = """
Hey,how are you?                     

I was just checking in.   
                                    All good?

"""
print(multiline)

# Escaping special charactors
# \ cancels special charactors
# \n new line
# \t add a tab
# \\ informs py it's just a normal slash
sentence = "I'm back at work!\tHey!\n\nWhere's this at\\located?"

print(sentence)


# String methods


print(first.lower())  # Make lower case
print(first.upper())  # Make upper case
print(first)

print(multiline.title())  # Make title case
print(multiline.replace("good", "ok"))  # replace a word
print(multiline)

print(len(multiline))  # get length of given sentence
multiline += "                               "
multiline = "                     " + multiline
print(len(multiline))

# removing the white space
print(len(multiline.strip()))
print(len(multiline.lstrip()))  # removing from the left side
print(len(multiline.rstrip()))  # removing from the right side

print("")

# Build a menu
title = "menu".upper()

print(title.center(20, "="))
print(
    "Coffee".ljust(16, ".") + "$1".rjust(4)
)  # fill 16 spaces from left with dots and 4 spaces right

print(
    "Muffin".ljust(16, ".") + "$2".rjust(4)
)  # fill 16 spaces from left with dots and 4 spaces right

print(
    "Cheesecake".ljust(16, ".") + "$4".rjust(4)
)  # fill 16 spaces from left with dots and 4 spaces right

print("")

# string index values
print(first[1])  # print the 2nd letter in the name
print(first[-1])  # print the last letter in the name
print(first[1:-1])  # print the 2nd to the last letter in the name
print(first[1:])  # get the value from the 2nd letter and onwards

print("")

# Working with boolean data return True or False

print(first.startswith("D"))  # does given name start with D
print(first.endswith("Z"))  # does given name end with Z

# Boolean data types ( True or False data)

myvalue = True
x = bool(False)

print("")

print(type(x))  # what type is x
print(isinstance(myvalue, bool))  # Is it a bool value

print("")

# Numeric data types
# int (interger)
price = 100
best_price = int(80)

print(type(price))  # what type is price
print(isinstance(best_price, int))  # Is it a int value

print("")

# float (have decimals)
gpa = 3.28
y = float(1.14)

print(type(gpa))  # what type is gpa
print(isinstance(y, float))  # Is it a float value


# complex (used in electrical engeneering)
comp_value = 3 + 4j  # using 'j' notation

print(type(comp_value))

# = extra property values
print(comp_value.real)  # real number value
print(comp_value.imag)  # imaginary number value

# builtin functions for numbers
print(abs(gpa))  # absolute value
print(abs(gpa * -1))  # absolute value to the nearest decimal float specified

print(round(gpa))  # round to the nearest integer
print(round(gpa, 1))  # round to the nearest decimal place specified

print("")

# Use of import math module
print(math.pi)
print(math.sqrt(64))  # squired root of number
print(math.ceil(gpa))  # ceiling of our gpa value
print(math.floor(gpa))  # floor of our gpa value


print("")

# Casting a string to a number
zipcode = "0025"
zip_value = int(zipcode)  # change string to int

print(type(zip_value))

# quick note
# Error if you attempt to cast incorrect data
# zip_value = int(Pretoria)
