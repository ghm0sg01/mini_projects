import random
from words import word_list


def game():
    while True:
        print("Welcome to Hangman!")
        tries = input("What difficulty level would you like? (Easy/Medium/Hard):\n").lower()
        if tries == 'easy':
            tries = 8
        elif tries == 'medium':
            tries = 6
        elif tries == 'hard':
            tries = 4

        # Convert word list to upper
        up_word_list = [x.upper() for x in word_list]

        # Secret word is chosen by random number in word_list
        rand_word = random.randrange(0, 2465)
        secret_word = (up_word_list[rand_word])
        # secret_word = "HELLOWORLD"

        guessed_letters = []
        wrong_letters = tries

        print("The word you have to guess is", len(secret_word), "letters long.") 

        while wrong_letters > 0:
            print("\n Your guesses:", guessed_letters)
            guess = input("Guess a letter: ").upper()
            if guess in guessed_letters:
                print("You have already guessed that letter.")
                continue
            elif guess in secret_word:
                print("Correct! There is at least one \"" + guess +  "\" in this word.")
            else:
                wrong_letters -= 1
                print("Incorrect! There are no " + guess + "'s in this word.", wrong_letters, "turn(s) left.")
                
            guessed_letters.append(guess)
            blank_letters = 0

            for x in secret_word:
                if x in guessed_letters:
                    print(x, end="")
                else:
                    print("_", end="")
                    blank_letters += 1

            if blank_letters == 0:
                print("\n You got it! The word was", secret_word, "and you got it in", len(guessed_letters), "tries!")
                play_again = input("Want to play again? y/n ")
                if play_again == 'y':
                    break
                else:
                    quit
        else:
            print("The word was", secret_word + ".")
            print("Thanks for playing!")
            play_again = input("Want to play again? y/n ")
            if play_again == 'y':
                break
            else:
                quit

game()
    

    