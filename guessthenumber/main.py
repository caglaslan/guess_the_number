import random
from art import logo

def guess_the_number():
    rand_number = random.randint(1,100)
    print(logo)
    print(rand_number)
    print("Welcome!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        remaining_attemps = 10
    elif difficulty == "hard":
        remaining_attemps = 5

    end_of_game = False

    while not end_of_game:
        print(f"You have {remaining_attemps} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if remaining_attemps == 0:
            print("You've run out of guesses, you lose.")
            end_of_game = True
        if guess == rand_number:
            print(f"You got it! The answer was {rand_number}.")
            end_of_game = True
        elif guess < rand_number:
            print("Too low.")
            remaining_attemps -= 1

        elif guess > rand_number:
            print("Too high.")
            remaining_attemps -= 1


guess_the_number()