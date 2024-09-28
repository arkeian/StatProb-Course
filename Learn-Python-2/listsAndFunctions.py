# Page 1
n = [1, 3, 5]

print(n[1])

# Page 2
n = [1, 3, 5]
n[1] *= 5
print(n)

# Page 3
n = [1, 3, 5]
n.append(4)
print(n)

# Page 4
n = [1, 3, 5]
n.pop(0)
print(n)

# Page 5
number = 5

def my_function(x):
  return x * 3

print(my_function(number))

# Page 6
m = 5
n = 13

def add_function(x, y):
  return x + y
  
print(add_function(m, n))

# Page 7
n = "Hello"
def string_function(s):
  return s + "world"

print(string_function(n))

# Page 8
def list_function(x):
  return x

n = [3, 5, 7]
print(list_function(n))

# Page 9
def list_function(x):
  return x[1]

n = [3, 5, 7]
print(list_function(n))

# Page 10
def list_function(x):
  x[1] += 3
  return x

n = [3, 5, 7]
print(list_function(n))

# Page 11
n = [3, 5, 7]
def list_extender(list):
  list.append(9)
  return list

print(list_extender(n))

# Page 12
n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print(x[i])

print_list(n)

# Page 13
n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] *= 2
  return x 

print(double_list(n))

# Page 14
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print(my_function(range(0, 3)))

# Page 15
n = [3, 5, 7]

def total(numbers):
  result = 0
  for number in numbers:
    result += number
  return result

# Page 16
n = ["Michael", "Lieberman"]
def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print(join_strings(n))

# Page 17
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
  return x + y

print(join_lists(m, n))

# Page 18
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print(flatten(n))