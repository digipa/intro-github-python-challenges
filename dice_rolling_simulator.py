# dice-rolling simulator
# 1. Dice Rolling Simulator

# The Goal: Like the title suggests, this project involves writing a program
# that simulates rolling dice. When the program runs, it will randomly choose
# a number between 1 and 6. (Or whatever other integer you prefer — the number
# of sides on the die is up to you.) The program will print what that number is.
# It should then ask you if you’d like to roll again. For this project, you’ll
# need to set the min and max number that your dice can produce. For the average die,
# that means a minimum of 1 and a maximum of 6. You’ll also want a function that
# randomly grabs a number within that range and prints it.

# import the random function
import random
# declare the minimum and maximum values of the die faces
dice_min = 1
dice_max = 6

# write a function to simulate rolling the dice using the random.randint() function
# then print the number on the dice
def roll_dice() :
    dice_face = random.randint(dice_min, dice_max)
    print("You rolled a " + str(dice_face))
    return

# declare a boolean to ask if user wants to play again
# we want it to be initially true to simulate a "do-while" loop
play_again = True

# while loop to simulate rolling the dice
while play_again:
    roll_dice()
    player = input("Play again? (y/n): ")
    if player == 'y':
        play_again = True
    else:
        play_again = False
    # call our roll_dice() function
