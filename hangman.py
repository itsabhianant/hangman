import random
from words import words
from hangman_visual import lives_visual_dict_easy, lives_visual_dict_hard, lives_visual_dict_medium, lives_visual_dict_impossible
import string


def get_valid_word(words):
    """Gets word from words.py wihtout '-' or ' '."""

    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    """Defines the logic of this program."""

    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = ask_for_level()

    if lives == 12:
        visual = lives_visual_dict_easy
    elif lives == 9:
        visual = lives_visual_dict_medium
    elif lives == 6:
        visual = lives_visual_dict_hard
    elif lives == 3:
        visual = lives_visual_dict_impossible

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


            #gets here when len(word_letters) == 0 or lives == 0

    if lives == 0:
        print(lives_visual_dict_easy[lives])
        print(f"Hahaha... he died... The word was {word}")
    else:
        print(f"Oh shoot... {word} saved him :-[")


def hangman_loop(end_char="q"):
    """
    We can choose whether to play the game again

    If the character string specified by end_char is entered, it can be finished
    """
    inputed_char = ""
    content = f"If you want to end this game, press {end_char}: "

    while True:
        inputed_char = input(content)
        if inputed_char != end_char:
            hangman()
        else:
            break

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
    hangman()
    hangman_loop()



#TODO:

# Add option to exit the game when asking for e, m, i, h.

# Add a score board that reflects points of the player after 
# completion of every game independent of the results or what input 
# player has given.A more advanced version will be if the program 
# distributes points on the basis of chances left to win the match
# For ex: If the player wins by 9 lives remaining in easy mode he/she 
# gets 9*1 points. If the player wins by 4 lives remaining in medium 
# mode he/she gets 5*5 points. If the player wins by 2 lives remaining
# in hard mode he/she gets 2*10 points. If the player wins by 1 life
# remaining in impossible mode he/she gets 1*15 points. It will be nice
# if the player sees the points he earned from a specific round and also
# what his total score is.

# Adjust the length of the word that is given for ex: if player selects
# easy than word length is >= 6
# medium than word length is >= 8
# medium than word length is >= 10
# impossible than word length is < 10
# Also add some words in words[] of words.py which has 10+ letters.

# Make test cases for this program.
