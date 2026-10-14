# Number Guessing Game

## Problem
Write a guessing game: pick a random number between 1 and 100, ask the user to guess, give feedback until they get it right, then print how many valid guesses it took.

## Function Signatures
`play_game(target=None, max_attempts=None)`

- `target`: optional `int` secret number (defaults to a random integer from 1 to 100)
- `max_attempts`: optional `int` for the bonus

## How to Run
```
python number_guessing_game.py
```

## Requirements
- pick a random integer between 1 and 100 (inclusive) at the start (unless `target` is provided)
- loop until the user guesses correctly
- on each guess, print `"too high"`, `"too low"`, or `"correct! you got it in X guesses"`
- count only **valid** guesses toward the total
- invalid input (non-integer, decimal, empty string, number outside 1–100) must print an error (e.g. `"invalid input"`) and ask again — do not crash, do not count it

## Example Session
```
guess a number between 1 and 100: hello
  invalid input. enter a whole number between 1 and 100.
guess a number between 1 and 100: 50
  too high
guess a number between 1 and 100: 25
  too low
guess a number between 1 and 100: 37
  correct! you got it in 3 guesses
```

## Assumptions
- valid guess = an integer in range 1–100 inclusive
- the game runs until the user wins — no forced exit

## Hint
What happens if you call `int()` on a string like `"abc"` or `"3.5"`? How would you catch that without crashing?

## Bonus
- add a maximum number of attempts (e.g. 7); if the user runs out, reveal the number and end the game
- after the game ends, ask if the user wants to play again
