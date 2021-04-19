import random
from words import words
from hangman_visual import lives_visual_dict_easy, lives_visual_dict_hard, lives_visual_dict_medium, \
    lives_visual_dict_impossible
import string

total_score = 0

def get_valid_word(words, lives):
    """Gets word from words.py wihtout '-' or ' '."""
    word = ""

    if lives == 12:
        word_dict = [word for word in words if len(word) >= 4 and len(word) <=6] 
        word = random.choice(word_dict)
    elif lives == 9:
        word_dict = [word for word in words if len(word) >=6 and len(word) <= 8]
        word = random.choice(word_dict)
    elif lives == 6:
        word_dict = [word for word in words if len(word) >=8 and len(word) <= 10]
        word = random.choice(word_dict)
    elif lives == 3:
        word_dict = [word for word in words if len(word) > 10]
        print(word_dict)
        word = random.choice(word_dict)

      # check for foul words
    while '-' in word or ' ' in word:
        word = random.choice(word_dict)

    return word.upper()

 
 
def hangman():
    """Defines the logic of this program."""

    global total_score

    lives = ask_for_level()
    word = get_valid_word(words, lives)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    if lives == 12:
        visual = lives_visual_dict_easy
        point = int(1)
    elif lives == 9:
        visual = lives_visual_dict_medium
        point = int(5)
    elif lives == 6:
        visual = lives_visual_dict_hard
        point = int(10)
    elif lives == 3:
        visual = lives_visual_dict_impossible
        point = int(15)

    while len(word_letters) > 0 and lives > 0:

        print(f"\nYou have {lives} lives left and you have used the letters:", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(visual[lives])
        print(f"Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print(f"\nYou have guessed the wrong letter... {user_letter} not in the word.")

        elif user_letter in used_letters:
            print("\nYou have already guessed that number.")

        else:
            print(f"{user_letter} is not a valid input.")

            # gets here when len(word_letters) == 0 or lives == 0

    if lives == 0:
        print(lives_visual_dict_easy[lives])
        print(f"Hahaha... he died... The word was {word}")
        print("\nYou got 0 points... LOL...XD")
    else:
        print(f"Oh shoot... {word} saved him :-[")
        score = point * lives
        total_score += score
        print(f"\nTake your freaking score...it's: {score}")


def terminate():
    print("terminate")
    print("see you again")


def hangman_handling(function=None):
    """When it is terminated with ctrl + c, it calls the function specified by the function argument and terminates
    If you use this, user's environment will not be displayed.
    """
    try:
        hangman()
        hangman_loop()
    except KeyboardInterrupt:
        if function:
            function()
        quit()


def hangman_loop(end_char="q"):
    """
    We can choose whether to play the game again
    If the character string specified by end_char is entered, it can be finished
    """
    inputed_char = ""
    content = f"\nIf you want to end this game, press {end_char}: "

    while True:
        inputed_char = input(content)
        if inputed_char != end_char:
            hangman_handling(terminate)
        else:
            print(f"your total score: {total_score}")
            quit()


def ask_for_level():
    """
    Asks the player how hard he/she wants the game to be and assigns
    lives accordingly.
    """

    while True:
        print("\n1) Easy (e): Lives: 12")
        print("2) Medium (m): Lives: 9")
        print("3) Hard (h): Lives: 6")
        print("4) Impossible (i): Lives: 3")

        level = input("\nSelect your level from above: ")
        if level == 'e':
            life = 12
            break
        elif level == 'm':
            life = 9
            break
        elif level == 'h':
            life = 6
            break
        elif level == 'i':
            life = 3
            break

        else:
            print("\nPlease choose a valid option\n")
            continue

    return life


if __name__ == '__main__':
    hangman_handling(terminate)

# TODO:


# It will be great if the program also displays the total score gained
# by a player in a single program run.

# Adjust the length of the word that is given for ex: if player selects
# easy than word length is >= 6
# medium than word length is >= 8
# medium than word length is >= 10
# impossible than word length is < 10
# Also add some words in words[] of words.py which has 10+ letters.

# Make test cases for this program.
