
import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("=== Number Guessing Game ===")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!\n")
    
    while True:
        try:
            # Prompt user for input
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Provide feedback
            if guess < target_number:
                print("Hint: Too low, try again.")
            elif guess > target_number:
                print("Hint: Too high, try again.")
            else:
                print(f"\n✅ Congratulations! You guessed the number {target_number}.")
                print(f"Total attempts: {attempts}")
                break
        
        except ValueError:
            # Handle invalid input gracefully
            print("⚠️ Invalid input. Please enter a valid integer.")

# Entry point
if __name__ == "__main__":
    number_guessing_game()
