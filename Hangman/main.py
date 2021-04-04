import random
from hangmanwords import words
from hangmanstates import hangman
import string
# A border to use to see output clearly
BORDER = "*" * 25


# Function to randomly pick word from the list
def get_word(wordlist: list) -> str:
    word_to_guess = random.choice(wordlist)
    while "-" in word_to_guess or " " in word_to_guess:
        word_to_guess = random.choice(wordlist)
    return word_to_guess


# Function to execute the hangman
def play(secret_word):
    user_word: str = "_" * len(secret_word)
    letters_used = ""
    while (secret_word != user_word) and (len(letters_used) < 8):

        print(hangman(len(letters_used)))
        print(f"{user_word}\n")
        print(BORDER)
        print(f"{letters_used}")

        letter = input("Enter a letter: ")

        if letter[0] in secret_word:
            if letter[0] not in letters_used or letter[0] not in user_word:
                for index in range(len(secret_word)):
                    if letter[0] == secret_word[index]:
                        user_word = user_word[:index] + letter[0] + user_word[index+1:]
        elif letter[0] in user_word or letter[0] in letters_used:
            print("Letter already used.")
        else:
            letters_used += letter[0]
        print(BORDER)
    if user_word == secret_word:
        print("Nice Job! ", end="")
    else:
        print("The man is dead. ", end="")
    print(f"The word is {secret_word}")


play(get_word(words))
