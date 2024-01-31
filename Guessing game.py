import random
import time

def display_welcome():
    print("Welcome to the game!")
    time.sleep(1)
    print("Choose a number between 1 and 100.")
    time.sleep(1)
    print("Your mission, should you choose to accept it, is to guess the number.")
    time.sleep(1)
    print("Lets see what you can do\n")

def get_teacher_guess():
    while True:
        try:
            guess = int(input("Take the guess: "))
            return guess
        except ValueError:
            print("Numbers Damn it!")

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = get_teacher_guess()
        attempts += 1

        if guess == secret_number:
            print(f"\nYou got the number! {secret_number} in {attempts} tries...")
            break
        elif guess < secret_number:
            print("Way too low buddy.")
        else:
            print("you gotta go down!.")
            

if __name__ == "__main__":
    display_welcome()
    play_game()
