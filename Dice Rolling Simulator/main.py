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
        return sided_dice


def main():
    dice_sides = get_dice_sides()
    print("You rolled an %d on the %d-sided die." % (randrange(1, dice_sides), dice_sides))

main()