# Page 1
"""
(ID) Tidak ada kode yang disertakan di dalam Page 1 karena belum diinstruksikan untuk membuat sebuah blok kode.
(EN) No codes are included within Page 1 because this page has yet to give the learner any instructions.
"""

# Page 2
# Define your spam function starting on line 5. You
# can leave the code on line 10 alone for now--we'll
# explain it soon!

def spam():
  """Prints 'Eggs!' to the console."""
  print("Eggs!")



# Define the spam function above this line.
spam()

# Page 3
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print("%d squared is %d." % (n, squared))
  return squared
  
# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

square(10)

# Page 4
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print("%d to the power of %d is %d.") % (base, exponent, result)

power(37, 4)  # Add your arguments here!

# Page 5
def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2

# Page 6
def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False
  
# Page 7
# Ask Python to print sqrt(25) on line 3.

print("sqrt(25)")

# Page 8
import math

print(math.sqrt(25))

# Page 9
# Import *just* the sqrt function from math on line 3!

from math import sqrt

# Page 10
# Import *everything* from the math module on line 3!
# Not recommended

from math import *

# Page 11
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything) # Prints 'em all!

# Page 12
def biggest_number(*args):
  print(max(args))
  return max(args)
    
def smallest_number(*args):
  print(min(args))
  return min(args)

def distance_from_zero(arg):
  print(abs(arg))
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

# Page 13
# Set maximum to the max value of any set of numbers on line 3!

maximum = max(1, 1.000008, -1)

print(maximum)

# Page 14
# Set minimum to the min value of any set of numbers on line 3!

minimum = min(1, 1.000008, -1)

print(minimum)

# Page 15
absolute = abs(-42)

print(absolute)

# Page 16
# Print out the types of an integer, a float,
# and a string on separate lines below.

i, j, k = 3, 3.14, "Three Point One Four"
print(type(i))
print(type(j))
print(type(k))

# Page 17
def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"

# Page 18
from math import sqrt

print(sqrt(13689))

# Page 19
def distance_from_zero(num):
  if isinstance(num, (int, float)):
    return abs(num)
  else:
    return "Nope"