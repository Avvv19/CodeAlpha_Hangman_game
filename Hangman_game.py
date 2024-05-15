#imports from random module
import random

#chooses a random word from a predefined word list
def choose_word():
    words = ["vijay", "arun", "raghavendra", "manoj", "keerthi", "friends", "anandroi"]
    return random.choice(words)

#It displays the hangman figure based on wrong guesses   
def open_hangman(wrong_guesses):
    # Your implementation of the hangman figure display goes here
    return "Hangman figure unavailable."

#This function is the loop for Hangman.
def play_hangman():
    
    #Choose a random word from list words
    word = choose_word()
    #Checks the word to a set of letters 
    word_letters = set(word)
    #Create a set containing all lowercase letters of the alphabet
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    #empty set to store guessed letters
    used_letters = set()
    #number of wrong guesses
    wrong_guesses = 0

    #game loop
    while len(word_letters) > 0 and wrong_guesses < 6:

        print(open_hangman(wrong_guesses))
        print("Current Word: ", ' '.join([letter if letter in used_letters else '_' for letter in word]))

        #user input for a letter guess
        while True:
            user_letter = input("Guess a letter: ").lower()
            #Check if the input is a valid single letter
            if user_letter in alphabet - used_letters:
                break
            else:
                print("You already guessed that letter. Please try again.")
        #Add the guessed letter to the set of used letters
        used_letters.add(user_letter)

        #if the guess is correct
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        #Increment the number of wrong guesses
        else:
            wrong_guesses += 1 

    #Game over message
    if wrong_guesses == 6:
        print(open_hangman(wrong_guesses))
        print("You lost The word was:", word)
    else:
        print("Congratulations You guessed the word:", word)

# Start the game
play_hangman()

