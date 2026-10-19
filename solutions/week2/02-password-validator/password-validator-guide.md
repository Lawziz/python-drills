# Solving Password Validator in Python

A password is only useful if it's hard to guess. Many websites enforce rules to make sure of that.

In this exercise, a password is valid only if it follows all `five` of these rules:

1. It has at least 8 characters.
2. It has at least one uppercase letter (A–Z).
3. It has at least one lowercase letter (a–z).
4. It has at least one digit (0–9).
5. It has at least one special character, like `!` or `@`.

> We will write one small function for each rule, then combine them into a final function called `is_valid_password`.

### For example:

```python
is_valid_password("Hello@12")   # True, all 5 rules pass
is_valid_password("hello@12")   # False, no uppercase letter
is_valid_password("Hi@1")       # False, fewer than 8 characters
```

> Every function must **return** `True` or `False`. It must not print anything. The tests check the value your function returns.

## Tools you need

### 1. Looping through a string

A string is a series of characters, so you can loop over it with a `for` loop, one character at a time:

```python
for char in "Hi!":
    print(char)
```

> This prints `H`, then `i`, then `!`.

### 2. String methods that check a character

Python strings come with built-in checks. Each one returns `True` or `False`:

```python
"A".isupper()    # True, it is an uppercase letter
"a".isupper()    # False
"a".islower()    # True, it is a lowercase letter
"7".isdigit()    # True, it is a digit
"a".isalnum()    # True, it is a letter or a digit (alphanumeric)
"@".isalnum()    # False, it is neither a letter or a digit
" ".isspace()    # True, it is whitespace
```

### 3. `return` ends the function immediately

When Python reaches a `return`, the function stops right there. Nothing after it runs. We will use this to stop searching as soon as we find what we need.

## Step by step solution
### Step 1: Minimum length

This one needs no loop. `len()` gives the number of characters in a string, and we check if it is at least `8` character length:

```python
def has_min_length(password: str) -> bool:
    return len(password) >= 8
```

The comparison `len(password) >= 8` already gives us `True` or `False`, so we can return it directly.

```python
has_min_length("abcdefgh")   # True, 8 characters
has_min_length("abcdefg")    # False, 7 characters
```

### Step 2: At least one uppercase letter

The rule says *at least one*. That means we don't need to check every character. As soon as we find one uppercase letter, we know the answer is `True`.

**Here is the plan**:

1. Look at each character one by one.
2. If a character is uppercase, return `True` right away.
3. If we reach the end without finding one, return `False`.

```python
def has_uppercase(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False
```

Let's walk through `has_uppercase("hEllo")`:

1. `h`: is it uppercase? No. Move on.
2. `E`: is it uppercase? Yes. Return `True` and stop. The remaining letters are never checked.

Now `has_uppercase("hello")`:

1. We check `h`, `e`, `l`, `l`, `o`. None are uppercase.
2. The loop ends, so the last line runs and returns `False`.

### A common mistake

It's tempting to write this:

```python
def has_uppercase(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
        else:
            return False   # wrong!
```

The code above `ONLY` checks the **first** character, because `return False` ends the function straight away. With `"hEllo"`, it looks at `h`, sees it isn't uppercase, and returns `False` without ever reaching `E`.

**The fix?**

`return False` after the whole loop has finished and found nothing.

> That's why `return False` sits outside the loop, lined up with the `for`.

### Step 3: Lowercase and digit

These work the same way. Only the check inside the `if` changes:

```python
def has_lowercase(password: str) -> bool:
    for char in password:
        if char.islower():
            return True
    return False


def has_digit(password: str) -> bool:
    for char in password:
        if char.isdigit():
            return True
    return False
```

## Step 4: Special character

First we need to define "special". In this exercise, a `special` character is any character that is **not** a letter, **not** a digit, and **not** whitespace.

- `isalnum()` tells us if a character is a letter or a digit, so `not char.isalnum()` means it is neither.
- `char.isspace()` tells us if it is whitespace, so `not char.isspace()` means it is not.

We need both conditions to be true, so we join them with `and`:

```python
def has_special(password: str) -> bool:
    for char in password:
        if not char.isalnum() and not char.isspace():
            return True
    return False
```

**Let's check a few:**

```python
has_special("abc!")          # True, "!" is not a letter, digit, or space
has_special("Hello World")   # False, the space doesn't count
has_special("a_b")           # True, "_" is not a letter or digit
```

## Note: A shorter way with `any()`

Steps 2 to 4 all repeat the same pattern: `loop`, `check`, return `True` if found, otherwise return `False`.

Python has a built-in function for exactly this called `any()`.

`any()` looks at a series of `True` and `False` values and returns `True` if **at least one** is `True`. Like our loop, it stops as soon as it finds one.

### Here is `has_uppercase` rewritten with `any()`:

```python
def has_uppercase(password: str) -> bool:
    return any(char.isupper() for char in password)
```

**Read the inside part like a sentence:**

*"for each `char` in `password`, is it uppercase?"* 

That produces a `True` or `False` for every character, and `any()` tells us if at least one of them was `True`.

It does the same job as the loop version in one line. The two versions are equivalent, so use whichever you find easier to read.

If you're just starting out, the loop version is a great way to understand what is happening. `any()` is a shortcut you'll see a lot in real code.

## Step 5: Putting it together

Now for the final function. The rule is that **all five** checks must pass, so we join them with `and`:

```python
def is_valid_password(password: str) -> bool:
    return (
        has_min_length(password)
        and has_uppercase(password)
        and has_lowercase(password)
        and has_digit(password)
        and has_special(password)
    )
```

Notice that `is_valid_password` doesn't repeat any of the checking logic. It simply **calls** the five functions we already wrote. This has two benefits:

- It's easy to read. The function reads almost exactly like the rules.
- If a rule changes later (say, the minimum length becomes 10), you fix it in one place.

Also, `and` stops at the first `False`. If the password is too short, Python never bothers running the other four checks.

## Test it

```python
print(is_valid_password("Hello@12"))   # True
print(is_valid_password("hello@12"))   # False, no uppercase
print(is_valid_password("Hi@1"))       # False, too short
print(is_valid_password(""))           # False, fails every rule
```

> An empty password returns `False` because there are no characters to find, so every loop ends without returning `True`.

## Bonus: Which rules failed?

A message like "invalid password" isn't very helpful. It's better to tell the user which rules they broke. The bonus function returns a list with the name of each rule that failed.

### The plan:

1. Start with an empty list called `failed`.
2. Check each rule. If it fails, add its name to the list with `.append()`.
3. Return the list.

```python
def get_failed_requirements(password: str) -> list[str]:
    failed = []

    if not has_min_length(password):
        failed.append("min_length")
    if not has_uppercase(password):
        failed.append("uppercase")
    if not has_lowercase(password):
        failed.append("lowercase")
    if not has_digit(password):
        failed.append("digit")
    if not has_special(password):
        failed.append("special")

    return failed
```

> Did you notice the code above uses separate `if` statements, not an `if ... elif` chain?

With `elif`, Python would stop at the first failure. We want to check **every** rule, so each one gets its own `if`.

The order of the checks also matters. The exercise wants the names in this exact order, and writing the checks in that order gives it to us.

```python
get_failed_requirements("Hello@12")   # []
get_failed_requirements("hello@12")   # ["uppercase"]
get_failed_requirements("abc")        # ["min_length", "uppercase", "digit", "special"]
```

## Recap

- A string can be looped over one character at a time.
- To find out if *at least one* character matches, loop and `return True` as soon as you find it. Put `return False` after the loop.
- `any(... for char in password)` is a shorter way to write that same loop.
- Build small functions that each do one job, then combine them with `and`.
- Use separate `if` statements, not `elif`, when you want to check every condition.
- Return the answer. Don't print it.