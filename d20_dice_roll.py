from curses.ascii import isdigit
import random


armor_class = input("What is the creature's armor class? ")

if armor_class.isdigit():
    armor_class = int(armor_class)

    if armor_class <= 0:
        print("Please provide an armor class above 0.")
        (quit)
else:
    print("Please type a number above 0.")
    (quit)
attack_bonus = input("What is your attack bonus? ")

if attack_bonus.isdigit():
    attack_bonus = int(attack_bonus)

    if attack_bonus <= -1:
        print("Please provide an attack bonus of at least 0.")
        quit()
else:
    print("Please type a number.")
    quit()

while True:
    dice_roll = input('Type "roll" to roll the dice. ')
    #check "roll" was entered
    if dice_roll == str("roll"):

        #new dice roll
        roll = (random.randrange(1, 21))
       
        #print what was rolled
        print("You rolled a " + str(roll) + ".")
         #comparing dice roll against armor class minus attack bonus
        if roll < armor_class - attack_bonus:
            print("You missed! Your attack roll was " + str(roll + attack_bonus) + " but you need at least " + str(armor_class) + "!")
        else:
            print("You hit! You needed a " + str(armor_class) + " and your attack roll was " + str(roll + attack_bonus) + "!")
    
    else:
        print('Please type "roll" to roll the dice.')

   
