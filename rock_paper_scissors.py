import random

user_score = 0
computer_score = 0
game_ties = 0
used_rock = 0
used_paper = 0
used_scissors = 0
computer_rock = 0
computer_paper = 0
computer_scissors = 0

options = ["rock", "paper", "scissors"]

#welcome message
print("Hello! Welcome to the game of Rock Paper Scissors!")

game_start = input("Would you like to play? ").lower()
if game_start == "yes":
    quit

while True:
    print("Your wins: " + str(user_score) + "  Computer wins: " + str(computer_score) + "  Ties: " + str(game_ties))
    user_input = input("Please choose Rock/Paper/Scissors or 'Q' to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    #counts how many times option is used by user
    if user_input == "rock":
        used_rock += 1
    if user_input == "paper":
        used_paper += 1
    if user_input == "scissors":
        used_scissors += 1

    random_number = random.randint(0, 2)
    # 0 = rock  1 = paper  2 = scissors

    #counts how many times option is used by computer
    if random_number == 0:
        computer_rock += 1
    if random_number == 1:
        computer_paper += 1
    if random_number == 2:
        computer_scissors += 1

    computer_pick = options[random_number]
    print("Computer picked " + computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        user_score += 1
        print("You won!")

    elif user_input == "paper" and computer_pick == "rock":
        user_score += 1
        print("You won!")

    elif user_input == "scissors" and computer_pick == "paper":
        user_score += 1
        print("You won!")
    
    elif user_input == computer_pick:
        game_ties += 1
        print("You tied!")
    
    else:
        computer_score += 1
        print("You lost!")

used_rock = str(used_rock)

#Quit screen with stats and scores, gives final win or lose
print("Here are the stats:")
print("You chose... \n Rock", used_rock, "times.  Paper", used_paper, "times.  Scissors", used_scissors, "times.")
print("The computer chose... \n Rock", computer_rock, "times.  Paper", computer_paper, "times.  Scissors", computer_scissors, "times.")
print("Final score: ", user_score, "to", computer_score, "with", game_ties, "ties.")
if user_score > computer_score:
    print("You won!")
elif user_score == computer_score:
    print("You tied!")
else:
    print("You lost!")
print("Thank you for playing!" )