
import random

hangman_words = ['crypt','banjo','blitz','vortex','zodiac','phlegm','lucky','absurd','equip','rhythm','scratch','zombie','icebox','waltz','jovial']
computer_choice = random.choice(hangman_words)
word = set(computer_choice)
dashed_word = "-"*len(computer_choice)
print(dashed_word)

guessed_letters = set()
correct_guess = set()

failed = 0
while failed < 6:
    try:
        guess = input('Guess a letter in the secret word: ')
        guessed_letters.add(guess)
        if guess not in computer_choice:
            failed = failed + 1
            print('Wrong guess')         
        elif guess in computer_choice:
            index = [i for i, letter in enumerate(computer_choice) if letter == guess]
            correct_guess.add(guess)
            print(f"Letter'{guess}' is found at the indexes: {', '.join(map(str, index))}")
            if sorted(correct_guess)== sorted(word):
                print(f'You won!the word was {computer_choice}')
                break
            else:
                print('Take another guess')
        else:
            if failed == 6:
                print(f'Game over! You lost. The word was {computer_choice}') 
    except ValueError:
        print('please enter a valid letter')
    

   