import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "development"]
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"Current word: {display}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    
    while incorrect_guesses < max_incorrect_guesses:
        display_current_state(word, guessed_letters)
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Sorry, you ran out of guesses. The word was: {word}")

hangman()
