#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>
#include <ctype.h>

#define MAX_WORD_LENGTH 30
#define MAX_GUESSES 6

// Hangman display based on lives left
void display_hangman(int lives) {
    const char *stages[] = {
        "_____\n|   |\n|    \n|    \n|    \n|_______\n",       // 6 lives
        "_____\n|   |\n|   o\n|    \n|    \n|_______\n",       // 5 lives
        "_____\n|   |\n|   o\n|   |\n|    \n|_______\n",       // 4 lives
        "_____\n|   |\n|   o\n|  /|\n|    \n|_______\n",       // 3 lives
        "_____\n|   |\n|   o\n|  /|\\\n|    \n|_______\n",     // 2 lives
        "_____\n|   |\n|   o\n|  /|\\\n|  / \n|_______\n",     // 1 life
        "_____\n|   |\n|   o\n|  /|\\\n|  / \\\n|_______\n"     // 0 lives
    };
    printf("%s\n", stages[MAX_GUESSES - lives]);
}


void display_word(const char *word, const bool guessed_letters[26]) {
    for (int i = 0; i < strlen(word); i++) {
        char ch = word[i];
        if (ch >= 'a' && ch <= 'z' && guessed_letters[ch - 'a']) {
            printf("%c ", ch);
        } else {
            printf("_ ");
        }
    }
    printf("\n");
}


bool did_guess_all_letters(const char *word, const bool guessed_letters[26]) {
    for (int i = 0; i < strlen(word); i++) {
        char ch = word[i];
        if (ch >= 'a' && ch <= 'z' && !guessed_letters[ch - 'a']) {
            return false;
        }
    }
    return true;
}

int main(void) {
    srand((unsigned int)time(NULL));

    const char *words[] = {
        "potato", "wagon", "cooperate", "seek", "sulphur", "center", "bounce",
        "ruin", "interference", "autonomy", "examination", "roof", "market",
        "pop", "light", "shock", "skin", "donor", "element", "execution",
        "vessel", "contrast"
    };
    int word_count = sizeof(words) / sizeof(words[0]);
    const char *word = words[rand() % word_count];

    bool guessed_letters[26] = { false };
    int lives = MAX_GUESSES;
    char guess;

    printf("Welcome to Hangman!\n");

    while (lives > 0) {
        printf("\nYou have %d lives left.\n", lives);
        display_word(word, guessed_letters);
        printf("Guess a letter: ");
        scanf(" %c", &guess);
        guess = tolower(guess);

        if (guess < 'a' || guess > 'z') {
            printf("Invalid input. Please enter a lowercase letter.\n");
            continue;
        }

        if (guessed_letters[guess - 'a']) {
            printf("You already guessed that letter.\n");
            continue;
        }

        guessed_letters[guess - 'a'] = true;

        if (strchr(word, guess)) {
            printf("Correct!\n");
        } else {
            printf("Incorrect.\n");
            lives--;
        }

        display_hangman(lives);

        if (did_guess_all_letters(word, guessed_letters)) {
            printf("\nCongratulations! You guessed the word '%s' with %d lives left!\n", word, lives);
            break;
        }
    }

    if (lives == 0) {
        printf("You lost. The word was '%s'.\n", word);
    }

    return 0;
}
