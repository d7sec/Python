# The Pig Latin translation machine
# Exercise / project for Chris Wolcott - this was made in Python 2, with convert to 3
pyg = 'ay'

original = input('Enter a word: ')

#Take the input and run it through the loop
if len(original) > 0 and original.isalpha():
  # Set word to all lower case
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  
  print (new_word)
  
else:
  print ('That is not an acceptable word')