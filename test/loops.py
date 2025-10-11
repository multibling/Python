"""
Test 3
Write a for loop that prints every number from 1 to 10,
but only prints the even numbers.

"""

for i in range(0, 10, 2):
    print(i)


"""
A couple of small tweaks if you want to match the original request exactly:

You started at 0, but the task said 1 to 10. If you want the numbers 2, 4, 6,
8, 10, start at 2 and go up to 11 (the upper bound is exclusive).

Here’s the adjusted loop:

`range(start, stop, step)` is exactly the right tool.
"""

for i in range(2, 11, 2):
    print(i)
