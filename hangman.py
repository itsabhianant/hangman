import random
from words import words
from hangman_visual import lives_visual_dict_easy, lives_visual_dict_hard, lives_visual_dict_medium, \
    lives_visual_dict_impossible
import string

total_score = 0

# words: list that stores all words in the collection
# lives: integer that stores the total lives a user has (based on the level chosen)
def get_valid_word(words, lives):
    """Gets word from words.py wihtout '-' or ' '."""
    word = ""

    # makes a new list of words based on their lengths 
    # and then chooses a word randomly from the new list
    if lives == 12:
        word_dict = [word for word in words if len(word) >= 4 and len(word) <= 6]
        word = random.choice(word_dict)
    elif lives == 9:
        word_dict = [word for word in words if len(word) >= 7 and len(word) <= 8]
        word = random.choice(word_dict)
    elif lives == 6:
        word_dict = [word for word in words if len(word) >= 9 and len(word) <= 10]
        word = random.choice(word_dict)
    elif lives == 3:
        word_dict = [word for word in words if len(word) > 10]
        word = random.choice(word_dict)

    # until a word contains ' ' or '-', choose another word randomly
    while '-' in word or ' ' in word:
        word = random.choice(word_dict)

    return word.upper()


def hangman():
    """Defines the logic of this program."""

    global total_score

    lives = ask_for_level() # saves the number of lives
    word = get_valid_word(words, lives) # gets a random word based on difficulty
    word_letters = set(word)    # makes a set of the letters of randomly chosen word
    alphabet = set(string.ascii_uppercase) #stores A-Z in alphabet
    used_letters = set()    # makes an empty set to store used letters

    # stores dictionary of lives visual (from hangman_visual.py) in visual
    # according to the difficulty of the game 
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

    # the loop breaks when either the lives become zero or the word is guessed
    while len(word_letters) > 0 and lives > 0:
        
        # prints the number of lives remaining and letters used
        print(f"\nYou have {lives} lives left and you have used the letters:", " ".join(used_letters))

        # prints the visual and letters guessed correctly in the word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(visual[lives])
        print(f"Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in word_letters:  # if the input letter is the right guess
                word_letters.remove(user_letter)
                print('')

            else:   # if the input letter is not the right guess
                lives = lives - 1
                print(f"\nYou have guessed the wrong letter... {user_letter} not in the word.")

        elif user_letter in used_letters:  # if the letter is already inputted
            print("\nYou have already guessed that number.")

        else:   # invalid letter
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

    # loop infinitely iterate until player chooses the difficulty i.e. e, m, h or i
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

# Make test cases for this program.

