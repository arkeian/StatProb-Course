# Page 1
count = 0

if count < 5:
    print(f"Hello, I am an if statement and count is {count}")

while count < 10:
    print(f"Hello, I am a while and count is {count}")
    count += 1

# Page 2
loop_condition = True

while loop_condition:
    print("I am a loop")  
    loop_condition = False

# Page 3
num = 1

while num <= 10:
    print(num ** 2)
    num += 1

# Page 4
choice = input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':
    choice = input("Sorry, I didn't catch that. Enter again: ")

# Page 5
count = 0

while count < 10:
    print(count)
    count += 1

# Page 6
count = 0

while True:
    print(count)
    count += 1
    if count >= 20:
        break
  
# Page 7
import random

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Sorry, you lose!")
        break
    count += 1
else:
    print("You win!")

# Page 8
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print("You win!")
        break
    guesses_left -= 1
else:
    print("You lose.")
  
# Page 9
print("Counting...")

for i in range(20):
    print(i)

# Page 10
hobbies = []

for i in range(3):
    hobbies.append(input())

print(hobbies)

# Page 11  
thing = "spam!"

for c in thing:
    print(c)

word = "eggs!"

for c in word:
    print(c)

# Page 12
phrase = "A bird in the hand..."

for char in phrase:
    if char.lower() == "a":
        print('X', end=' ')
    else:
        print(char, end=' ')

print()

# Page 13
numbers  = [7, 9, 12, 54, 99]

print("This list contains: ")

for num in numbers:
    print(num)

for num in numbers:
    print(num ** 2)

# Page 14
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    print(f"{key} {d[key]}")

# Page 15
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices, 1):
    print(index, item)

# Page 16
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print(a)
    else:
        print(b)

# Page 17
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for fruit in fruits:
  if fruit == 'tomato':
    print('A tomato is not a fruit!') # (It actually is.)
    break
  print('A', fruit)
else:
  print('A fine selection of fruits!')

# Page 18
fruits = ['banana', 'apple', 'orange', 'pear', 'grape']

print('You have...')
for fruit in fruits:
    if fruit == 'tomato':
        print('A tomato is not a fruit!') # (It actually is.)
        break
    print('A', fruit)
else:
    print('A fine selection of fruits!')

# Page 19
chars = "Tuhan pasti kan menunjukkan\nKebesaran dan kuasanya"

for char in chars:
    if char == " ":
        print("Your string has more than one word.")
        break
else:
    print("Your string is only one word.")