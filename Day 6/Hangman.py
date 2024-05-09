import random
import Hangman_art
import Hangman_words

from Hangman_art import stages

chosen_word = random.choice(Hangman_words.word_list)

display = []


for letter in chosen_word:
    display.append("_")

print(Hangman_art.logo)

end_of_game = False
lives = 6


while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        print(f"\n\nYou have already guessed {guess}, try again!")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        print(f"\n\n{guess} is not in the word! Try again!")

    print(stages[lives])
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("\nYou have won!\n")
    
    if lives == 0:
        end_of_game = True
        print("\nYou Lose!\n")