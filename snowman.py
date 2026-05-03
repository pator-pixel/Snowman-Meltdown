import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    # Stage 1
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    # Stage 2
    """
     ___  
    /___\\ 
    (o o) 
    """,
    # Stage 3
    """
     ___  
    /___\\ 
    """
]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])

    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    print("Word:", displayed_word.strip())
    print("Mistakes:", mistakes)

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected:", secret_word)  # später entfernen

    display_game_state(mistakes, secret_word, guessed_letters)

    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)

    print("You guessed:", guess)

if __name__ == "__main__":
    play_game()