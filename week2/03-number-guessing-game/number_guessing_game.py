
import random


def play_game(target=None, max_attempts=None):
   
   if max_attempts == None:
    max_attempts = 3
    
    if target == None:
        target = random.randint(1, 100)

    attempts_made = 0
    
    while attempts_made < max_attempts:

        user_input = input("guess a number between 1 and 100: ").strip()

        if not user_input.isdigit():
            print("Invalid input. enter a whole number between 1 and 100.")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("Invalid input. enter a whole number between 1 and 100.")
            continue

        attempts_made += 1

        if guess == target:
            print(f"Correct! you got it in {attempts_made} guesses.")
            return True
        
        elif guess < target:
            print("too low.")
        elif guess > target:
            print("too high.")

    print(f"game over! The number was {target}")
    return False

    
    
# Do not modify below this line
if __name__ == "__main__":
    play_game()

# while True:
#     play_again = input("Would you like to play again? (Y/N)").lower()

#     if play_again == "y":
#         play_game()

#     else:
#         break
