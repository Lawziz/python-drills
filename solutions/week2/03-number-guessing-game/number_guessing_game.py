import random


def play_game(target=None, max_attempts=None):
    target = random.randint(1, 100) if not target else target   # allow tests to inject a fixed target
    attempts = 0
    while True:
        if max_attempts and attempts >= max_attempts:           # check limit before prompting, not after
            print("Game over! you have exhausted number of attempts")
            print(f"The number is {target}")
            return False

        user_input = input("guess a number between 1 and 100: ")

        try:
            guess = int(user_input)
        except ValueError:                                      # catches anything that isn't a whole number
            print("invalid input. enter a whole number between 1 and 100.")
            continue

        if not (1 <= guess <= 100):
            print("invalid input. enter a whole number between 1 and 100.")
            continue

        attempts += 1                                           # only a valid guess counts as an attempt

        if guess == target:
            noun = "guess" if attempts == 1 else "guesses"     # singular on the first try
            print(f"correct! you got it in {attempts} {noun}")
            return
        elif guess < target:
            print("too low")
        else:
            print("too high")


# Do not modify below this line
if __name__ == "__main__":
    play_game()
