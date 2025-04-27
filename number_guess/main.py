import random

def guess(high):
    low = 1
    random_number = random.randint(low, high)
    guess = 0
    attempts = 0
    while guess != random_number:
        guess = int(input(f"Make a guess between {low} and {high}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.", random_number)
            low = guess + 1
            attempts += 1
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
            high = guess - 1
            attempts += 1

    print(f"Yay! You guessed the number correctly: {random_number}")
    print(f"It took you {attempts} attempts to guess the number.")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    attempts = 0
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low # could also be high, since low = high
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)?: ").lower()
        if feedback == "h":
            high = guess - 1
            attempts += 1
        elif feedback == "l":
            low = guess + 1
            attempts += 1

    print(f"Yay! The computer guessed your number {guess} correctly!")
    print(f"It took the computer {attempts} attempts to guess the number.")
        

guess(100)
        