# Password Validator

## Problem

Check whether a password meets all five security rules. Return `True` if all pass, `False` if any fail.

## The Rules

Write one function for each rule:

| Rule | Function | Returns `True` when... | Example |
|---|---|---|---|
| Length | `has_min_length` | there are **8 or more** characters (spaces count) | `"abcdefgh"` → `True`, `"abcdefg"` → `False` |
| Uppercase | `has_uppercase` | there is **at least one** letter from A–Z | `"hEllo"` → `True`, `"hello"` → `False` |
| Lowercase | `has_lowercase` | there is **at least one** letter from a–z | `"HELLo"` → `True`, `"HELLO"` → `False` |
| Digit | `has_digit` | there is **at least one** digit from 0–9 | `"abc1"` → `True`, `"abc"` → `False` |
| Special | `has_special` | there is **at least one** character that is not a letter, digit, or whitespace (like `!`, `@`, `_`) | `"abc!"` → `True`, `"abc 1"` → `False` |

## Function Signatures

```python
has_min_length(password: str) -> bool
has_uppercase(password: str) -> bool
has_lowercase(password: str) -> bool
has_digit(password: str) -> bool
has_special(password: str) -> bool
is_valid_password(password: str) -> bool
```

Each function takes a string and **returns** `True` or `False`. Don't print. The tests compare return values.

## Examples

| input | output | why |
|---|---|---|
| `is_valid_password("Hello@12")` | `True` | all 5 rules pass |
| `is_valid_password("hello@12")` | `False` | no uppercase letter |
| `is_valid_password("Hi@1")` | `False` | fewer than 8 characters |
| `has_special("Hello World")` | `False` | a space does not count as special |

## Requirements

- Implement all five `has_*` functions.
- Implement `is_valid_password` by **calling** them. Don't repeat their logic.
- The password is always a string. It can be empty.

## Hint

How would you check if *at least one* character in a string satisfies a condition? Start with a simple loop, then see if Python has a shorter way.

## Bonus

Implement `get_failed_requirements(password: str) -> list[str]`.

It returns the names of the rules that failed, always in this order: `"min_length"`, `"uppercase"`, `"lowercase"`, `"digit"`, `"special"`. It returns `[]` if the password is valid.

| input | output |
|---|---|
| `get_failed_requirements("Hello@12")` | `[]` |
| `get_failed_requirements("hello@12")` | `["uppercase"]` |
| `get_failed_requirements("")` | `["min_length", "uppercase", "lowercase", "digit", "special"]` |
