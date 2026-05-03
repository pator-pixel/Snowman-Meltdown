import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print("\n" + "=" * 30)
    print(STAGES[mistakes])

    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    print("Word: " + displayed_word.strip())
    print("Mistakes:", mistakes, "/", len(STAGES) - 1)

    if guessed_letters:
        print("Guessed letters:", ", ".join(guessed_letters))
    else:
        print("Guessed letters: none")

    print("=" * 30)

def play_round():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\nWelcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            mistakes += 1

        word_complete = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_complete = False

        if word_complete:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You saved the snowman!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("The snowman melted!")
    print("The secret word was:", secret_word)

def play_game():
    while True:
        play_round()

        play_again = input("\nDo you want to play again? (y/n): ").lower().strip()

        if play_again != "y":
            print("Thanks for playing Snowman Meltdown!")
            break