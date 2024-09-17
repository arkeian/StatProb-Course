# Page 1
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
  print(name)

# Page 2
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for key in webster:
  print(webster[key])

# Page 3
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for num in a:
  if num % 2 == 0:
    print(num)

# Page 4
# Write your function below!
def fizz_count(strings):
  count = 0
  for string in strings:
    if string == "fizz":
      count += 1
  return count

# Page 5
for letter in "Codecademy":
  print(letter)
    
# Empty lines to make the output pretty
print()
print()

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print(letter)

# Page 6 - 9
"""
(ID) Dari Page 6 ke 9, kodenya ditambahkan sedikit demi sedikit sampai terbentuk suatu program yang kohesif.
(EN) From Page 6 to 9, the code is added gradually until a complete program is constructed.
"""
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

for key in prices:
  print(key)
  print("price: %s" % prices[key])
  print("stock: %s" % stock[key])

total = 0
for key in prices:
  print(prices[key] * stock[key])
  total += prices[key] * stock[key]

print(total)

# Page 10
groceries = ["banana", "orange", "apple"]

# Page 11
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    total += prices[item]
  return total

# Page 12
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total

# Page 13
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

print(compute_bill(shopping_list))

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total