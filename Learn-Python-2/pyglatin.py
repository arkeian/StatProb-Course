# Page 1
"""
(ID) Tidak ada kode yang disertakan di dalam Page 1 karena belum diinstruksikan untuk membuat sebuah blok kode.
(EN) No codes are included within Page 1 because this page has yet to give the learner any instructions.
"""

# Page 2
print("Pig Latin")

# Page 3
print('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word: ")

# Page 4
print('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word: ")

if len(original) > 0:
  print(original)
else:
  print("empty")

# Page 5
print('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word: ")

if len(original) > 0 and original.isalpha():
  print(original)
else:
  print("empty")

# Page 6
"""
(ID) Tidak ada kode yang disertakan di dalam Page 6 karena instruksinya hanya menjalankan blok kode Page 5.
(EN) No codes are included within Page 6 because this page instructs the learner to run Page 5's block of code.
"""

# Page 7
pyg = "ay"

# Page 8
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print(original)
else:
  print('empty')

word = original.lower()
first = word[0]

# Page 9
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print(original)
else:
  print('empty')

word = original.lower()
first = word[0]
new_word = "%s%s%s" % (word, first, pyg)

# Page 10
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print(original)
else:
  print('empty')

word = original.lower()
first = word[0]
new_word = "%s%s%s" % (word[1:len(word)], first, pyg)

# Page 11
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print(original)
else:
  print('empty')

word = original.lower()
first = word[0]
new_word = "%s%s%s" % (word[1:len(word)], first, pyg)

print(new_word)