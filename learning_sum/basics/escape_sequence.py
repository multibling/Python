# Normal Characters
'''
A B C

5 9 0

@ ?
'''

# Special Characters
'''
\" \' \\

\n \t

-- To include quotes in the text
\" - double quote

\' - single quote

-- To include a real backslash in the text
\\ - backslash

-- To create a new line
\n - new line

-- To add a horizontal tab
\t - tab: to have spaces between words

-- For back spaces
\b - backspaces
'''

# Inform python some qoutes are part of massage
print("Hi \"Python\"")

print('Hi "Python"')    # this also works

# Print a path to something
print("Path: C:\\Users\\Bling")

'''
It moves the text that comes after Special Character
to the new line.
'''
# Adding a new line between prints
print("massage1")
print()
print("massage2")

# can also be writen this way
print("massage1\n")
print("massage2")

# Adding 3 new lines
print("massage1\n\n\n")
print("massage2")


# Can be done this way
print("massage1\n\n\nMassage2")
print("massage3")

# Adding a Tab space between words
print("massage1\tMassage2")

# Python challenge
print("Your Learning Path:\n\t- Python Basics\n\t- Data Engineering\n\t- AI")

# """ Allows us to write text in multiple line string
# the new line syntex is note needed when using this method
print("""Your Learning Path:
      \t- Python Basics
      \t- Data Engineering
      \t- AI""")

'''
PYTHON()
- Built-in Python function
- Displays massages in output for user
- Use Cases:
        - Communicate
        - Show Results Debugg
        - Test
'''
