import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    
    secret_number = random.randint(1, 50)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! 📈 Try guessing higher.")
            elif guess > secret_number:
                print("Too high! 📉 Try guessing lower.")
            else:
                print(f"🎉 Spot on! You guessed it in {attempts} attempt(s)!")
                break
        except ValueError:
            print("❌ Invalid input! Please enter a whole number.")

if __name__ == "__main__":
    number_guessing_game()