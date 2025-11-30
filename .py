import random

def number_guessing_game():
    print("----- Number Guessing Game -----")
    number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess it!\n")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("❌ Please enter a valid number.\n")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("🔼 Too low! Try a higher number.\n")
        elif guess > number:
            print("🔽 Too high! Try a lower number.\n")
        else:
            print(f"🎉 Correct! The number was {number}.")
            print(f"You guessed it in {attempts} attempts.\n")
            break

number_guessing_game()
