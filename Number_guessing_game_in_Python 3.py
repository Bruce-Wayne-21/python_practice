import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Your guess must be between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid integer.")

def categorize(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    elif 20 <= age < 65:
        return "Adult"
    else:
        return "Senior"

if __name__ == "__main__":
    # Run the categorize demo
    result = categorize(25)
    print(f"Age 25 is categorized as: {result}")

    # # Start the number guessing game
    # number_guessing_game()

