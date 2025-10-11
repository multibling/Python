# Exercise 3: Time Conversion
# Convert 3725 seconds into hours, minutes, and remaining seconds.
import math

total_seconds = 3725
# Use floor division and modulus operators

# floor division
min = math.floor(total_seconds / 60)
print(min)

print("")

hours = math.floor(min / 60)
print(hours)

print("")

# modulus
sec_min_left = total_seconds % 60
sec_hour_left = total_seconds % 60
sec_left = sec_hour_left + sec_min_left
print(sec_left)

print("")

# actual code
hours2 = total_seconds // (60 * 60)
minutes = total_seconds % (60 * 60) // 60
seconds = total_seconds % 60
print(hours2, "Hours")
print(minutes, "minutes")
print(seconds, "seconds")
