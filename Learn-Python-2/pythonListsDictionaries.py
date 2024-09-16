# Page 1
zoo_animals = ["pangolin", "cassowary", "sloth", "komodo dragon"];
# One animal is missing!

if len(zoo_animals) > 3:
  print("The first animal at the zoo is the " + zoo_animals[0])
  print("The second animal at the zoo is the " + zoo_animals[1])
  print("The third animal at the zoo is the " + zoo_animals[2])
  print("The fourth animal at the zoo is the " + zoo_animals[3])

# Page 2
numbers = [5, 6, 7, 8]

print("Adding the numbers at indices 0 and 2...")
print(numbers[0] + numbers[2])
print("Adding the numbers at indices 1 and 3...")
print(numbers[1] + numbers[3])

# Page 3
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
zoo_animals[3] = "komodo dragon"

# Page 4
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.extend(["shirts", "trousers", "medicines"])


list_length = len(suitcase) # Set this to the length of suitcase

print(f"There are {list_length} items in the suitcase.")
print(suitcase)

# Page 5
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last = suitcase[4:]

# Page 6
animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]

# Page 7
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")

# Your code here!
animals.insert(duck_index, "cobra")

print(animals) # Observe what prints after the insert operation

# Page 8
my_list = [1,9,3,8,5,7]

for number in my_list:
  print(number * 2)

# Page 9
start_list = [5, 3, 1, 2, 4]

# Your code here!
square_list = sorted([num ** 2 for num in start_list])


print(square_list)

# Page 10
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print(residents['Puffin']) # Prints Puffin's room number

# Your code here!
print(residents["Sloth"])
print(residents["Burmese Python"])

# Page 11
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print(menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu["Nasi Padang"] = 4.50
menu["Nasi Liwet"] = 4.00
menu["Nasi Goreng"] = 4.50


print("There are " + str(len(menu)) + " items on the menu.")
print(menu)

# Page 12
# key - animal_name : value - location 
zoo_animals = {
  'Unicorn' : 'Cotton Candy House',
  'Sloth' : 'Rainforest Exhibit',
  'Bengal Tiger' : 'Jungle House',
  'Atlantic Puffin' : 'Arctic Exhibit',
  'Rockhopper Penguin' : 'Arctic Exhibit'
}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Tristan da Cunha'


print(zoo_animals)

# Page 13
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print(backpack)

# Page 14
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].remove('dagger')
inventory['backpack'].sort()
inventory['gold'] += 50