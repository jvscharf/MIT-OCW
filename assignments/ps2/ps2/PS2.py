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
    print(len(wordlist), "words loaded.")
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
    count = 0
    for l in secret_word:
        if l in letters_guessed:
            count += 1
    if count == len(secret_word):
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word_new = []
    for l in secret_word:
        if l in letters_guessed:
            secret_word_new.append(l)
        else:
            secret_word_new.append('_')
    return ' '.join(secret_word_new)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    list_letters = list(string.ascii_lowercase)
    list_letters_copy = list_letters[:]
    for l in letters_guessed:
        if l in list_letters_copy:
            list_letters_copy.remove(l)
    return ''.join(list_letters_copy)
    
def unique_letters(secret_word):
    
    secret_word_list = list(secret_word)
    secret_word_list_unique = []
    for l in secret_word_list:
        if l not in secret_word_list_unique:
            secret_word_list_unique.append(l)
    return len(secret_word_list_unique)

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
    word_length = len(secret_word)
    available_guesses = 6
    letters_guessed = []
    num_warnings = 3
    print (secret_word)
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word", word_length, "letters long.")
    print ('-------------------------------------------------------')
    print ("You have", available_guesses, "guesses left.")
    print ("Available letters:", get_available_letters(letters_guessed))
    while available_guesses >= 0 and is_word_guessed(secret_word, letters_guessed) == False:
        new_letter = input('Please guess a letter: ').lower()
        if new_letter not in list(string.ascii_lowercase):
            if num_warnings >= 1:   
                num_warnings -= 1
                print ('Not a valid letter. You have', num_warnings, 'warnigs left:', get_guessed_word(secret_word, letters_guessed))
                print ("You have", available_guesses, "guesses left.")
            else:
                if available_guesses < 1:
                    print ('Sorry, you ran out of guesses. The word was', secret_word,'.')
                    break
                else:
                    available_guesses -= 1
                    print ('You already guessed that letter. You lose a guess:', get_guessed_word(secret_word, letters_guessed))
                    print ("You have", available_guesses, "guesses left.")
        elif new_letter not in get_available_letters(letters_guessed):
            if num_warnings >= 1:   
                num_warnings -= 1
                print ('You already guessed that letter. You have', num_warnings, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                print ("You have", available_guesses, "guesses left.")
            else:
                if available_guesses < 1:
                    print ('Sorry, you ran out of guesses. The word was', secret_word,'.')
                    break
                else:
                    available_guesses -= 1
                    print ('You already guessed that letter. You lose a guess:', get_guessed_word(secret_word, letters_guessed))            
                    print ("You have", available_guesses, "guesses left.")
        elif new_letter in secret_word:
            letters_guessed.append(new_letter)
            print ('Good guess: ', get_guessed_word(secret_word, letters_guessed))
            print ("You have", available_guesses, "guesses left.")
        else:
            letters_guessed.append(new_letter)
            print ('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            if new_letter in ['a','e','i','o','u']:
                if available_guesses < 2:
                    print ('Sorry, you ran out of guesses. The word was', secret_word,'.')
                    break
                else:
                    available_guesses -= 2
                    print ("You have", available_guesses, "guesses left.")
            else:
                if available_guesses < 1:
                    print ('Sorry, you ran out of guesses. The word was', secret_word,'.')
                    break
                else:
                    available_guesses -= 1
                    print ("You have", available_guesses, "guesses left.")
        print ("Available letters:", get_available_letters(letters_guessed))
        print ('-------------------------------------------------------')
    
    total_score = available_guesses * unique_letters(secret_word)
    if is_word_guessed(secret_word, letters_guessed):
        print ('Congratlations, you won!')
        print ('Your total score for this game is', total_score)


#When you've completed your hangman function, scroll down to the bottom
#of the file and uncomment the first two lines to test
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
    my_word = my_word.replace(' ','')
    my_word_list = list(my_word)
    other_word_list = list(other_word)
    if len(my_word_list) != len(other_word_list):
        return False
    else:
        for i in range(len(my_word_list)):
            if my_word_list[i] != '_':
                if my_word_list[i] != other_word_list[i]:
                    return False
            elif my_word_list.count(other_word_list[i]) > 0:
                return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    possible_words = []
    for i in wordlist:
        if match_with_gaps(my_word, i) == True:
            possible_words.append(i)
    print ('Possible matches: ', possible_words)
    

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
    word_length = len(secret_word)
    available_guesses = 6
    letters_guessed = []
    num_warnings = 3
    print (secret_word)
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word", word_length, "letters long.")
    print ('-------------------------------------------------------')
    print ("You have", available_guesses, "guesses left.")
    print ("Available letters:", get_available_letters(letters_guessed))
    while available_guesses >= 0 and is_word_guessed(secret_word, letters_guessed) == False:
        new_letter = input('Please guess a letter: ').lower()
        if new_letter == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif new_letter not in list(string.ascii_lowercase):
            if num_warnings >= 1:   
                num_warnings -= 1
                print ('Not a valid letter. You have', num_warnings, 'warnigs left:', get_guessed_word(secret_word, letters_guessed))
                print ("You have", available_guesses, "guesses left.")
            else:
                if available_guesses < 1:
                    print ('Sorry, you ran out of guesses. The word was', secret_word,'.')
                    break
                else:
                    available_guesses -= 1
                    print ('You already guessed that letter. You lose a guess:', get_guessed_word(secret_word, letters_guessed))
                    print ("You have", available_guesses, "guesses left.")
        elif new_letter not in get_available_letters(letters_guessed):
            if num_warnings >= 1:   
                num_warnings -= 1
                print ('You already guessed that letter. You have', num_warnings, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                print ("You have", available_guesses, "guesses left.")
            else:
                if available_guesses < 1:
                    print ('Sorry, you ran out of guesses. The word was', secret_word,'.')
                    break
                else:
                    available_guesses -= 1
                    print ('You already guessed that letter. You lose a guess:', get_guessed_word(secret_word, letters_guessed))            
                    print ("You have", available_guesses, "guesses left.")
        elif new_letter in secret_word:
            letters_guessed.append(new_letter)
            print ('Good guess: ', get_guessed_word(secret_word, letters_guessed))
            print ("You have", available_guesses, "guesses left.")
        else:
            letters_guessed.append(new_letter)
            print ('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            if new_letter in ['a','e','i','o','u']:
                if available_guesses < 2:
                    print ('Sorry, you ran out of guesses. The word was', secret_word,'.')
                    break
                else:
                    available_guesses -= 2
                    print ("You have", available_guesses, "guesses left.")
            else:
                if available_guesses < 1:
                    print ('Sorry, you ran out of guesses. The word was', secret_word,'.')
                    break
                else:
                    available_guesses -= 1
                    print ("You have", available_guesses, "guesses left.")
        print ("Available letters:", get_available_letters(letters_guessed))
        print ('-------------------------------------------------------')
    
    total_score = available_guesses * unique_letters(secret_word)
    if is_word_guessed(secret_word, letters_guessed):
        print ('Congratlations, you won!')
        print ('Your total score for this game is', total_score)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

secret_word = choose_word(wordlist)
#hangman(secret_word)
hangman_with_hints(secret_word)
