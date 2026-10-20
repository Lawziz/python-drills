# Solving FizzBuzz in Python

## What FizzBuzz asks

You are given a number `n`. Your job is to build a list with one item for every number from 1 to `n` (including `n`). Each item follows these rules:

- If the number is divisible by 3, put `"Fizz"` in the list instead of the number.
- If the number is divisible by 5, put `"Buzz"` instead.
- If the number is divisible by both 3 and 5, put `"FizzBuzz"` instead.
- Otherwise, put the number in the list as a string.

For example, `fizzbuzz(5)` gives:

```python
["1", "2", "Fizz", "4", "Buzz"]
```

`3` is divisible by 3 so it got replaced with `"Fizz"`, and `5` is divisible by 5 so it got replaced with `"Buzz"`. The other numbers stay as strings.

> **Note**: The function must **return** the list, not print it. The tests check the value your function returns.

## Two tools you need

### 1. `range()`

`range()` gives you a series of numbers you can loop over, one at a time. It takes a `start` and a `stop`:

```python
range(1, 4)   # gives 1, 2, 3
```

Notice that 4 is **not** included. `range` counts up to the stop number but never reaches it. So to include `n` in our loop, we write `range(1, n + 1)`.

> `range` also has an optional third value called `step`, which sets how big each jump is. We don't need it here.

### 2. The modulo operator `%`

`%` gives you the remainder after a division.

```python
5 % 2   # gives 1, because 2 goes into 5 twice, with 1 left over
6 % 3   # gives 0, because 3 goes into 6 exactly, with nothing left over
7 % 3   # gives 1, because 3 goes into 7 twice, with 1 left over
```

This is how we check divisibility. If `i % 3 == 0`, there is no remainder, so `i` is divisible by 3.

## Why the order of the checks matters

When Python reads an `if ... elif ... else` chain, it checks the conditions from top to bottom. As soon as one is true, it runs that block and **skips the rest**.

Let's see what happens to the number 15, which is divisible by both 3 and 5.

**a. Wrong order (checking 3 first):**

1. Is `15 % 3 == 0`? Yes, so add `"Fizz"`.
2. Python skips every other check.

We get `"Fizz"`, but we wanted `"FizzBuzz"`.

**b. Right order (checking "both" first):**

1. Is `15 % 3 == 0` **and** `15 % 5 == 0`? Yes, so add `"FizzBuzz"`.

That's the correct answer. The rule is to put the most specific check first.

## Building the solution step by step

### Step 1: The skeleton

The problem says to return a list, so I start by creating an empty list and returning it.

A `list` holds multiple items in order, so it's the right place to collect our answers.

```python
def fizzbuzz(n: int) -> list[str]:
    result = []

    return result
```

### Step 2: Loop through the numbers

We know exactly where the loop starts (1) and ends (`n`), so a `for` loop is a good fit. A `while` loop is better when you don't know when to stop.

`.append()` adds an item to the end of the list.

At this point, the function just returns every number as a string.

```python
def fizzbuzz(n: int) -> list[str]:
    result = []

    for i in range(1, n + 1):
        result.append(str(i))

    return result
```


### Step 3: Add the checks

Now we replace some numbers with words. Remember the order: "both" comes first.

```python
def fizzbuzz(n: int) -> list[str]:
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result
```

**Here is what each part does:**

- `if i % 3 == 0 and i % 5 == 0`: both 3 and 5 divide `i`, so add `"FizzBuzz"`.

- `elif i % 3 == 0`: only 3 divides `i`, so add `"Fizz"`.
- `elif i % 5 == 0`: only 5 divides `i`, so add `"Buzz"`.
- `else`: neither divides `i`, so add the number as a string.

## Test it

```python
print(fizzbuzz(5))   # ["1", "2", "Fizz", "4", "Buzz"]
print(fizzbuzz(1))   # ["1"]
print(fizzbuzz(0))   # []
```

`fizzbuzz(0)` returns an empty list because `range(1, 1)` has nothing to loop over. Our function handles this without any extra code.

## Recap

- `range(1, n + 1)` loops from 1 to `n`, because the stop number is never included.
- `%` gives the remainder, and a remainder of 0 means divisible.
- In an `if ... elif` chain, Python stops at the first true condition, so check "both" first.
- Return the list. Don't print it.
