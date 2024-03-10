import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    tries = 0
    max_tries = 10

    print("I'm thinking of a number between 1 and 100. Can you guess it? You have 10 tries.")

    while tries < max_tries:
        guess = int(input("Enter your guess: "))
        tries += 1

        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {tries} tries.")
            break

    if guess != number:
        print(f"Sorry, you ran out of tries. The number was {number}.")

# Run the game
guess_the_number()
