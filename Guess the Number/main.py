from random import randrange

def generate_number():
    return randrange(1,100)

def parse_user_input():
    user_guess = 0

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            break
        except ValueError:
            print("Not a valid number! Please try again... ")

    if user_guess == 0 || user_guess > 100:
        print ("It has to be a guess BETWEEN 1 and 100")
        return parse_user_input()
    else:
        return user_guess


def main():
    number_to_guess = generate_number()


main()