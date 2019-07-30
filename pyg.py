# The Pig Latin translation machine
# Exercise / project for Chris Wolcott - this was made in Python 2, with convert to 3

# Set pyg variable to get called in the concatenation string
pyg = 'ay'

# Users input to store in the original variable
original = input('Enter a word: ')

# Take the input Original variable and run it through the loop
# Check to make sure the Original variable has characters and are only letters

while True:
    if len(original) > 0 and original.isalpha():

        # Take Original variable, make is all lower case and pass it to word variable
        word = original.lower()

        # Take first letter of word variable, make new variable called first
        first = word[0]

        # Combine the created variables to form a new concatenation string
        new_word = word + first + pyg

        # New variable to print, which just starts the new_word Variable at character 1 otherwise it prints out original WORD variable
        new_word = new_word[1:len(new_word)]

        print (new_word)
    else:
        print ('That is not an acceptable word')
    break
