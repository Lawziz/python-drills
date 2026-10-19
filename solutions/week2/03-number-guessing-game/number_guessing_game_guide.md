# Solving the Number Guessing Game in Python

## What we're building

The computer picks a secret number between 1 and 100. You keep guessing, and after each guess it tells you if you are too high or too low. When you get it right, it tells you how many guesses it took.

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

Notice the first line: `hello` is not a valid guess, so the game shows an error and asks again. It must **not** crash, and it must **not** count that attempt.

> We will write two functions: `get_valid_input` to ask for a guess until it is valid, and `play_game` to run the game.

## Tools you need

### 1. `random.randint()`

`random.randint(1, 100)` gives a random whole number between 1 and 100. Unlike `range()`, **both ends are included**. You need `import random` at the top of your file.

### 2. `input()` always gives you a string

Even if the user types `50`, `input()` gives you the string `"50"`, not the number 50. To compare it with the secret number, we need to turn it into an integer with `int()`.

But `int()` crashes if the text isn't a whole number:

```python
int("50")    # 50
int("hello") # ValueError: crashes the program
int("3.5")   # ValueError: crashes the program
```

So we must check the text **before** we call `int()`.

### 3. `isdigit()`

`isdigit()` returns `True` only if every character in the string is a digit:

```python
"50".isdigit()      # True
"hello".isdigit()   # False
"3.5".isdigit()     # False, the "." is not a digit
"-5".isdigit()      # False, the "-" is not a digit
"".isdigit()        # False, an empty string has no digits
```

> That one check catches letters, decimals, negative numbers, and empty input.

### 4. `while True`, `continue`, `break` and `return`

- `while True` repeats forever, until something stops it.
- `continue` skips the rest of the current round and goes back to the top of the loop.
- `break` leaves the loop, but the function keeps running after it.
- `return` ends the whole function immediately.

## Step 1: Getting a valid guess

### The plan:

1. Ask the user for a guess.
2. If it isn't a whole number, print an error and ask again.
3. If it is outside 1 to 100, print an error and ask again.
4. Otherwise, return the guess as an integer.

```python
def get_valid_input():
    while True:
        user_input = input("guess a number between 1 and 100: ")

        if not user_input.isdigit():
            print("  invalid input. enter a whole number between 1 and 100.")
            continue

        if int(user_input) <= 0 or int(user_input) > 100:
            print("  invalid input. enter a whole number between 1 and 100.")
            continue

        return int(user_input)
```

The first `if` asks "is it a whole number?". The second asks "is it out of range?".

**The order matters**: the second check calls `int()`, and it only runs if the first check passed, so it can never crash.

The second `if` reads as: "the number is 0 or lower, **or** it is above 100." Those are the only two ways to be out of range.

### Let's walk through three inputs:

1. `"hello"`: `isdigit()` is `False`, so `not` makes the first `if` true. The error prints and `continue` asks again.
2. `"150"`: it passes the first check. In the second, `150 <= 0` is `False` but `150 > 100` is `True`, so the `or` is true. Error, ask again.
3. `"50"`: it passes the first check. In the second, `50 <= 0` is `False` and `50 > 100` is `False`, so the `or` is false. We skip both `if`s and reach `return 50`.

> A common slip is writing `int(user_input) < 0` instead of `<= 0`. That lets `0` through as a valid guess, because `0` is not less than `0`. Since `isdigit()` already rejects negative numbers, `0` is the only number below 1 that reaches this check, so it matters.

### The same range check with `not`

We can write the second `if` another way:

```python
if not (0 < int(user_input) <= 100):
```

`0 < int(user_input) <= 100` is a chained comparison.

**It reads like normal math:** "0 is less than the number, **and** the number is at most 100". In other words, "the number is in range".

`not` flips that: "the number is **not** in range".

> a number is not in range if it is 0 or lower, **or** above 100.

That is exactly what the first version said.

### Here is the proof with a few numbers:

| number | `number <= 0 or number > 100` | `not (0 < number <= 100)` |
|---|---|---|
| `0` | `True` (error) | `True` (error) |
| `1` | `False` (valid) | `False` (valid) |
| `50` | `False` (valid) | `False` (valid) |
| `100` | `False` (valid) | `False` (valid) |
| `101` | `True` (error) | `True` (error) |

> Both give the same answer every time, so we can use whichever is easier for us to read.

### Merging into one `if`

Our two checks print the same error and do the same `continue`, so we can join them with `or`:

```python
# Before: two separate checks
if not user_input.isdigit():
    print("  invalid input. enter a whole number between 1 and 100.")
    continue

if not (0 < int(user_input) <= 100):
    print("  invalid input. enter a whole number between 1 and 100.")
    continue

# After: one check
if not user_input.isdigit() or not (0 < int(user_input) <= 100):
    print("  invalid input. enter a whole number between 1 and 100.")
    continue
```

> Read it as: "if it's not a whole number, **or** it's not in range, show the error."

It still can't crash. Python reads `A or B` from left to right and stops as soon as it knows the answer. If the input isn't a whole number, the left side is `True`, so Python never runs the `int()` on the right.

### Making it easier to read

Instead of listing what can go wrong, we can describe what a **valid** guess looks like and put `not` in front:

```python
if not (user_input.isdigit() and (0 < int(user_input) <= 100)):
    print("  invalid input. enter a whole number between 1 and 100.")
    continue
```

It gives the same result because both versions say the same thing:

> a guess is bad if **either** check fails, and good only if **both** pass.

Let `A` be "it is a whole number" and `B` be "it is in range":

| `A` | `B` | `not A or not B` | `not (A and B)` |
|---|---|---|---|
| yes | yes | `False` (valid) | `False` (valid) |
| yes | no | `True` (error) | `True` (error) |
| no | yes | `True` (error) | `True` (error) |
| no | no | `True` (error) | `True` (error) |

The columns match in every row. And `and` also stops at the first `False`, so `int()` is just as safe here. This version is easier to read: "if it's not a valid guess, show an error."

### The final function

```python
def get_valid_input():
    while True:
        user_input = input("guess a number between 1 and 100: ")

        if not (user_input.isdigit() and (0 < int(user_input) <= 100)):
            print("  invalid input. enter a whole number between 1 and 100.")
            continue

        return int(user_input)
```

## Step 2: Running the game

Now `play_game`. It takes two optional values:

- `target`: the secret number. If we don't give one, the game picks a random number. (Giving one is handy for testing.)
- `max_attempts`: a limit on guesses. If we don't give one, the game has no limit. We'll use this in the bonus.

### Here is the core of the game, without the limit:

```python
def play_game(target=None, max_attempts=None):
    count = 0
    if target is None:
        target = random.randint(1, 100)

    while True:
        guess = get_valid_input()
        count += 1

        if guess < target:
            print("  too low")
        elif guess > target:
            print("  too high")
        else:
            print(f"correct! you got it in {count} guesses")
            return
```

### How it works:

- `count` starts at 0 and goes up by 1 only after `get_valid_input()` gives us a valid guess. Invalid input never leaves that function, so it is never counted.
- We compare the guess to the target. Too small means "too low", too big means "too high", and anything else must be a match.
- On a match, we print the result and `return`. This ends the function, which ends the loop.

## Bonus: Maximum attempts

Now let's use `max_attempts`. If it is `None`, there is no limit. If it is a number, the game stops when the user has used up that many guesses.

We only need to change the loop condition:

```python
while max_attempts is None or count < max_attempts:
```

Read it as: "keep going if there is no limit, **or** if we haven't used all our attempts yet."

If the loop ends without a win, the user ran out of attempts, so we reveal the number.

### Here is the full function:

```python
import random

def play_game(target=None, max_attempts=None):
    count = 0
    if target is None:
        target = random.randint(1, 100)

    while max_attempts is None or count < max_attempts:
        guess = get_valid_input()
        count += 1

        if guess < target:
            print("  too low")
        elif guess > target:
            print("  too high")
        else:
            print(f"correct! you got it in {count} guesses")
            return

    print("game over! you have used all your attempts")
    print(f"the number was {target}")
```

> The last two lines only run when the loop finishes without a win, because a win ends the function with `return`.

---

### A common mistake

It's tempting to use `break` instead of `return` when the user wins:

```python
        else:
            print(f"correct! you got it in {count} guesses")
            break   # wrong!

    print("game over! you have used all your attempts")
    print(f"the number was {target}")
```

`break` only leaves the loop. The function keeps going, so the "game over" message prints **even when the user wins**:

```
correct! you got it in 3 guesses
game over! you have used all your attempts
the number was 37
```

The fix is `return`. It ends the whole function, so nothing after the loop runs on a win.

---

### Using `break` the right way

If you prefer `break`, you can still make it work by adding an `else` to the loop:

```python
    while max_attempts is None or count < max_attempts:
        guess = get_valid_input()
        count += 1

        if guess < target:
            print("  too low")
        elif guess > target:
            print("  too high")
        else:
            print(f"correct! you got it in {count} guesses")
            break
    else:
        print("game over! you have used all your attempts")
        print(f"the number was {target}")
```

A loop can have its own `else`. It runs **only when the loop ends on its own**, which means the loop condition became `False` because the attempts ran out. If the loop is left with `break`, the `else` is skipped.

So the two cases work out like this:

- **The user wins:** `break` leaves the loop, the `else` is skipped, and no "game over" message appears.
- **The user runs out of attempts:** the condition becomes `False`, the loop ends normally, and the `else` runs.

> Look at where the `else` is. It lines up with `while`, not with the `if` inside the loop. That's how Python knows it belongs to the loop.

Both versions behave the same way. Use `return` if you want the simplest option, or `break` with `else` if you want the "out of attempts" message to live next to the loop.

## Test it

```python
play_game(target=37)                  # plays until you guess 37
play_game(target=37, max_attempts=3)  # you only get 3 valid guesses
```

To play with a random number, run the file:

```
python number_guessing_game.py
```

## Recap

- `input()` always gives a string. Check it with `isdigit()` before calling `int()`.
- `A and B` and `A or B` both stop as soon as the answer is known, so `isdigit()` protects `int()` from crashing.
- `not (0 < x <= 100)` is the same as `x <= 0 or x > 100`. Be careful with `<=`.
- `not (A and B)` is the same as `not A or not B`: a guess is bad if either check fails.
- `continue` goes back to the top of the loop. `return` ends the function. `break` only leaves the loop.
- A loop's `else` runs only if the loop ends without `break`.
- Only count a guess after it has been validated.
