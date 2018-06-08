from random import randrange

def get_dice_sides():
    sided_dice = 0

    while True:
        try:
            sided_dice = int(input("How many sides should the dice have? "))
            break
        except ValueError:
            print("That is not a valid number. Please try again.")

    if sided_dice == 0:
        print("A dice needs at least one side! Try again: ")
        return get_dice_sides()
    else:
        return print ("You rolled a %d on the %d-sided die." % (randrange(1, sided_dice), sided_dice))

get_dice_sides()