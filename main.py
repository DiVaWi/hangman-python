import random

possible_words = ['becode']
word_to_find = list(random.choice(possible_words))

def play(word_to_find):
    possible_words = ['becode']
    word_to_find = list(random.choice(possible_words))
    lives = 5
    correctly_guessed_letters = []
    wrongly_guessed_letters = []
    to_display = list(len(word_to_find) * "_")
    turn_count = 0
    error_count = 0
    word_is_found = False

    # Starting the game
    print("\nLet's play HANGMAN")
    print(' '.join(to_display))

    # Game is played as long as the user has still chances left en the word isn't yet be guessed
    while lives > 0 and word_is_found == False:

        # User gives the input
        guessed_letter = input("Please guess a letter: ")

        # Input-check: it should be 1 letter of the alphabet, if not, an error is shown in the else-statement
        if len(guessed_letter) == 1 and guessed_letter.isalpha():

            # Letter is previously guessed? Lookup in 2 lists (correctly and wrongly)
            if guessed_letter in correctly_guessed_letters or guessed_letter in wrongly_guessed_letters:
                print("You already tried the letter", guessed_letter)
                lives -= 1
                error_count += 1
                print("(You have", lives, "chances left...)")
                print("\n", ' '.join(to_display))

            # Letter is in the word ?
            elif guessed_letter in word_to_find:
                correctly_guessed_letters.append(guessed_letter)

                # Look for same character when multiple times in the word
                indices = [i for i, letter in enumerate(word_to_find) if letter == guessed_letter]
                for index in indices:
                    to_display[index] = guessed_letter

                # Show all the characters guessed so far
                to_display[word_to_find.index(guessed_letter)] = guessed_letter
                print("\n", ' '.join(to_display))
                turn_count += 1

                # Word is completely found
                if word_to_find == to_display:
                    well_played(turn_count, error_count)
                    break

            # Letter NOT in word: store the guessed letter
            else:
                wrongly_guessed_letters.append(guessed_letter)
                print("The letter", guessed_letter, "is not used in the word")
                lives -= 1
                error_count += 1
                turn_count += 1
                print("(You have", lives, "chances left...)")
                print("\n", ' '.join(to_display))

        # Input is not validated as 1 alphabetical letter
        else:
            print("Input is not valid\n")

    game_over()

def game_over():
    print("\n------- Game over -------")

def well_played(turn_count, error_count):
    word_is_found = True
    print(f"You found the word: {''.join(word_to_find)} in {turn_count} turns with {error_count} errors!")

def main():
    word_to_find = list(random.choice(possible_words))
    play(word_to_find)
    while input("Play again? (Y/N) ").upper() == "Y":
        word_to_find = list(random.choice(possible_words))
        play(word_to_find)

if __name__ == "__main__":
    main()