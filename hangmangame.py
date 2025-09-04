import random

def get_word():
    words = ["python", "complicated", "hangman", "challenge", "algorithm", "variable", "function", "exception", "iteration", "condition"]
    return random.choice(words).upper()

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[6 - tries]

def play_hangman():
    word = get_word()
    word_letters = set(word)
    guessed_letters = set()
    guessed_words = set()
    tries = 6

    print("Welcome to Complicated Hangman!")
    print(display_hangman(tries))
    print("_ " * len(word))

    while tries > 0 and len(word_letters) > 0:
        guess = input("Guess a letter or the whole word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.add(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.add(guess)
                word_letters.discard(guess)
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.add(guess)
            else:
                word_letters.clear()
        else:
            print("Invalid guess.")

        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print(display_hangman(tries))
        print(" ".join(word_display))
        print(f"Tries left: {tries}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Guessed words: {', '.join(sorted(guessed_words))}")
        print()

    if len(word_letters) == 0:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you lost. The word was: {word}")
        print("would you like to play again? (yes/no)")
    play_again = input().lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    play_hangman()