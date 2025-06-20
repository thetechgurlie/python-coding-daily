"""
Hangman (CLI - Command Line Interface Version) 🎯
------------------------
Guess the letters of a hidden fruit name.
Each wrong guess costs a life and draws part of the hangman.
Guess the word before the stickman is complete!

"""
import random # imported the random module
# ASCII Art
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")

# hangman stages based on number of wrong attempts

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Game setup
fruits = ['apple', 'mango', 'cherry', 'litchi', 'watermelon', 'kiwi'] # List of words
chosen_word = random.choice(fruits) # random.choice() randomly selects one fruit from the list of fruits
display = ["_"] * len(chosen_word) # list multiplication generates underscores based on length of the chosen word
lives = 6 #initally 6 lives assigned
guessed_letters = set() # To keep a track of guessed letters

# initial blank
print("\nWord: " + " ".join(display)) # .join displays underscores separated by a space into a string

# game loop
while True:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another.")
        continue
    guessed_letters.add(guess)

    if guess in chosen_word: # enters the loop only if the guess is present in the chosen word
        for i, letter in enumerate(chosen_word): # enumerate gets the index and the letter together 
            if letter == guess:
                display[i] = letter
    else:
        lives -= 1
        print(stages[6 - lives])
        if lives == 0:
            print("You lost! The word was:", chosen_word)
            break

    # shows the updated word on the same line each time a guess is made
    print("\nWord: " + " ".join(display))

    if "_" not in display:
        print("You win!!")
        break
