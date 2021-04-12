import random
from words import words
from hangman_visual import lives_visual_dict
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

    lives = 7

    while len(word_letters) > 0 and lives > 0:

        print(f"\nYou have {lives} chance left and you have used the letters:", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
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
        print(lives_visual_dict[lives])
        print(f"Hahaha... he died... The word was {word}")
    else:
        print(f"Oh shoot... {word} saved him :-[")

if __name__ == '__main__':
    hangman()