# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # check if letter in secret_word is contained in the letters_guessed list
    for l in secret_word:
        if l not in letters_guessed:
            return False
        
    return True
        
#secret_word = 'apple'
#letters_guessed = ['a', 'p', 'l', 'r', 'e', 's']
#print(is_word_guessed(secret_word, letters_guessed))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_string = ''
    for l in secret_word:
        if l not in letters_guessed:
            guessed_string += '_ '
        elif l in letters_guessed:
            guessed_string += l
    
    return guessed_string

#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_available = ''
    all_letters = string.ascii_lowercase
    for l in all_letters:
        if l not in letters_guessed:
            letters_available += l
    
    return letters_available
    
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_available_letters(letters_guessed))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('The word you are looking for has', len(secret_word), 'letters.')
    print('You will have 6 guesses to find the word.')
    print('You have 3 warnings left')
    print('-----------------------------------------')
    
    
    num_guesses = 6
    letters_guessed = []
    warnings = 3
    is_guessed = False
    while num_guesses > 0 and is_guessed == False:
        
        print('You have', num_guesses, 'guesses remaining')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = str(input('Please guess a letter: '))
        guess = str.lower(guess)
        
        if str.isalpha(guess) == False:
            warnings -= 1
            print('Your guess was not in the alphabet')
            if warnings < 0:
                num_guesses -= 1
                print('You have 0 warnings remaining')
            else:
                print('You have', warnings, 'warnings remaining')
        elif guess in letters_guessed:
            warnings -= 1
            print('You have already guessed this letter')
            if warnings < 0:
                num_guesses -= 1
                print('You have 0 warnings remaining')
            else:
                print('You have', warnings, 'warnings remaining')
        elif guess in secret_word:
            letters_guessed.append(guess)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print('Good guess:', guessed_word)
        elif guess not in secret_word:
            letters_guessed.append(guess)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print('Oops! That letter is not in my word:', guessed_word)
            if guess in 'aeiou':
                num_guesses -= 2
            else:
                num_guesses -= 1
        
        print('-------------------------------------------------')
        is_guessed = is_word_guessed(secret_word, letters_guessed)
            
        
    if is_guessed == True:
        guesses_remaining = num_guesses
        unique = []
        for char in secret_word:
            if char not in unique:
                unique.append(char)
        number_unique_letters = len(unique)
        total_score = guesses_remaining * number_unique_letters
        print('Congrats! You have found the word.')
        print('Your total score to this game is:', total_score)
    elif is_guessed == False:
        print('You ran out of guesses. The word is', secret_word)
            



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    
    if len(my_word) != len(other_word):
        return False
    
    for i in range(len(my_word)):
#        print('my_word:', my_word[i], 'other_word:', other_word[i])
        if my_word[i] != other_word[i] and my_word[i] != '_':
            return False
        
    return True

#print(match_with_gaps("te_ t", "tact"))
#print(match_with_gaps("a_ _ le", "banana"))
#print(match_with_gaps("a_ _ le", "apple"))
#print(match_with_gaps("a_ ple", "apple"))


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    found_word = False
    
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=' ')
            found_word = True
    
    if found_word == False:
        print("No matches found")
    print('\n')
        
#show_possible_matches("t_ _ t")
#show_possible_matches("abbbb_ ")
#show_possible_matches("a_ pl_ ")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('The word you are looking for has', len(secret_word), 'letters.')
    print('You will have 6 guesses to find the word.')
    print('You have 3 warnings left')
    print('-----------------------------------------')
    
    
    num_guesses = 6
    letters_guessed = []
    warnings = 3
    is_guessed = False
    guessed_word = ''
    while num_guesses > 0 and is_guessed == False:
        

        print('You have', num_guesses, 'guesses remaining')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = str(input('Please guess a letter: '))
        guess = str.lower(guess)
        
        if guess == '*':
            print("Possible word matches are:")
            show_possible_matches(guessed_word)
        elif str.isalpha(guess) == False:
            warnings -= 1
            print('Your guess was not in the alphabet')
            if warnings < 0:
                num_guesses -= 1
                print('You have 0 warnings remaining')
            else:
                print('You have', warnings, 'warnings remaining')
        elif guess in letters_guessed:
            warnings -= 1
            print('You have already guessed this letter')
            if warnings < 0:
                num_guesses -= 1
                print('You have 0 warnings remaining')
            else:
                print('You have', warnings, 'warnings remaining')
        elif guess in secret_word:
            letters_guessed.append(guess)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print('Good guess:', guessed_word)
        elif guess not in secret_word:
            letters_guessed.append(guess)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print('Oops! That letter is not in my word:', guessed_word)
            if guess in 'aeiou':
                num_guesses -= 2
            else:
                num_guesses -= 1
        
        print('-------------------------------------------------\n')
        is_guessed = is_word_guessed(secret_word, letters_guessed)
            
        
    if is_guessed == True:
        guesses_remaining = num_guesses
        unique = []
        for char in secret_word:
            if char not in unique:
                unique.append(char)
        number_unique_letters = len(unique)
        total_score = guesses_remaining * number_unique_letters
        print('Congrats! You have found the word.')
        print('Your total score to this game is:', total_score)
    elif is_guessed == False:
        print('You ran out of guesses. The word is', secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    secret_word = 'hello'
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)