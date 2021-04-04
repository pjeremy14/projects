# Function to show hangman state
def hangman(wrong_guesses: int) -> str:
    hangman_states = {
        0: "-----+\n"
           "     |\n"
           "     |\n"
           "     |\n",
        1: "-----+\n"
           "  O  |\n"
           "     |\n"
           "     |\n",
        2: "-----+\n"
           "  O  |\n"
           "  |  |\n"
           "     |\n",
        3: "-----+\n"
           "  O  |\n"
           " /|  |\n"
           "     |\n",
        4: "-----+\n"
           "  O  |\n"
           " /|\\ |\n"
           "     |\n",
        5: "-----+\n"
           "  O  |\n"
           " /|\\ |\n"
           "     |\n",
        6: "-----+\n"
           "  O  |\n"
           " /|\\ |\n"
           " /   |\n",
        7: "-----+\n"
           "  O  |\n"
           " /|\\ |\n"
           " / \\ |\n",
        8: "xxxxx+\n"
           "  Ø  X\n"
           " /|\\ X\n"
           " / \\ X\n",
    }
    return hangman_states[wrong_guesses]
