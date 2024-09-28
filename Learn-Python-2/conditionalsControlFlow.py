# Page 1
"""
(ID) Tidak ada kode yang disertakan di dalam Page 1 karena instruksinya hanya menjalankan program.
(EN) No codes are included within Page 1 because this page instructs the learner to run the given program.
"""

# Page 2
# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

# Page 3
# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False

# Page 4
# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 12 >= pow(12, 5)

# Make me true!
bool_three = isinstance("Hello, World!", str)

# Make me false!
bool_four = 4 == round(3.1415)

# Make me true!
bool_five = isinstance(12 / 3, float)

# Page 5
"""
(ID) Tidak ada kode yang disertakan di dalam Page 5 karena instruksinya hanya membaca tabel operasi boolean.
(EN) No codes are included within Page 5 because this page instructs the learner to read the boolean operations table.
"""

# Page 6
bool_one = False

bool_two = False

bool_three = False

bool_four = True

bool_five = True

# Page 7
bool_one = True

bool_two = True

bool_three = False

bool_four = True

bool_five = False

# Page 8
bool_one = False

bool_two = True

bool_three = True

bool_four = True

bool_five = False

# Page 9
bool_one = False

bool_two = True

bool_three = True

bool_four = True

bool_five = False

# Page 10
# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = True or not pow(2, 5) == int(pow(4, 3) / 2)

# Make me false!
bool_three = not not ((not False and not True) or (not not (False and True) or False and not (False or not True)))

# Make me true!
bool_four = abs(12 - 20) == pow(2, 3) and isinstance("True", str)

# Make me true!
bool_five = (-(-(pow(0, 10)))) == -1 + 1 and True

# Page 11
response = "Y"

answer = "Left"
if answer == "Left":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")
    
# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

# Page 12
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print(using_control_once())
print(using_control_again())

# Page 13
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False
    
# Page 14
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))

# Page 15
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))
