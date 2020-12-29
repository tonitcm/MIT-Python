# Problem Set 2, hangman.py
# Name: Antonio
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

#Starts Here

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    for word in secret_word:
        if word not in letters_guessed:
            return False
    return True

#print(is_word_guessed("cf", ["a", "c", "f", "g"]))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    guessed = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += "_"
    return guessed

#secret_word = "apple"
#letters_guessed = ["i", "e", "k", "p", "r", "s"]
#print(get_guessed_word(secret_word, letters_guessed))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    import string
    letter_list = list(string.ascii_lowercase)

    guessed = ""
    for letter in letters_guessed: #takes each letter from letters_guessed from letter_list
        if letter in letter_list:
          letter_list.remove(letter)
    for char in letter_list: #transforms output into joined code instead of a list format putting everything into a string
        guessed += char
    return guessed


#letters_guessed = []
#print(get_available_letters(letters_guessed))


def hangman(secret_word):

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long")
    print(secret_word)

    num_guesses = 6
    guesses = ""
    warning = 4
    vowel = list("aeiou")



    while num_guesses > 0:

        tries = input("Guess a letter:").lower()

        if tries in secret_word:
            guesses += tries
            letters_guessed.append(tries)
            print("Well done")
            print("You still have " + str(num_guesses) + " chances left")
            print("You have this letters available: " + get_available_letters(letters_guessed))
            print("Good guess " + get_guessed_word(secret_word, letters_guessed))
        else:
            if not tries.isalpha(): #isalpha returns true if all character in tries are alphabetical if not false otherwise
                warning = warning - 1
                print(
                    "That is not a letter you have " + str(warning) + " warnings left: " + get_guessed_word(secret_word,letters_guessed))
                if warning <= 0:
                    num_guesses = num_guesses - 1
                    print("You have " + str(num_guesses) + " chances left")
            else:
                print("Try again")
                #if the vowel is wrong you will lose 2 chances instead of 1
                if tries in vowel:
                    num_guesses = num_guesses - 2
                    letters_guessed.append(tries)
                    print("You still have " + str(num_guesses) + " chances left")
                    print("You have this letters available: " + get_available_letters(letters_guessed))
                else:
                    num_guesses = num_guesses - 1
                    letters_guessed.append(tries)
                    print("You have " + str(num_guesses) + " chances left")
                    print("You have guessed this letters: " + get_available_letters(letters_guessed))
                    print("Oops that letter is not in my word " + get_guessed_word(secret_word, letters_guessed))



        #if one of these gets to 0 game is over
        if num_guesses == 0:
           print("Sorry, you ran out of guesses, the secret word is " + secret_word)
        elif is_word_guessed(secret_word, letters_guessed): #if statement only work with true or false
            print("Congratulations")
            break
    return guesses


letters_guessed = []
secret_word = choose_word(wordlist)
get_guessed_word(secret_word, letters_guessed)
get_available_letters(letters_guessed)
hangman(secret_word)



# -----------------------------------


