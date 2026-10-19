# Password Validator

## Problem

A password is only valid if it follows five security rules. Your job is to write one small function for each rule, then combine them into a single function that decides whether a password is valid.

Return `True` if the password passes all five rules, and `False` if it fails any of them.

## The Five Rules

| Rule | Function | Returns `True` when... | `True` example | `False` example |
|---|---|---|---|---|
| Minimum length | `has_min_length` | the password has **8 or more** characters (spaces count) | `"abcdefgh"` | `"abcdefg"` |
| Uppercase | `has_uppercase` | there is **at least one** uppercase letter (A–Z) | `"hEllo"` | `"hello"` |
| Lowercase | `has_lowercase` | there is **at least one** lowercase letter (a–z) | `"HELLo"` | `"HELLO"` |
| Digit | `has_digit` | there is **at least one** digit (0–9) | `"abc1"` | `"abc"` |
| Special | `has_special` | there is **at least one** special character | `"abc!"` | `"abc 1"` |

### What counts as a special character?

A special character is any character that is **not** a letter, **not** a digit, and **not** whitespace.

- Special: `! @ # $ % ^ & * ( ) - _ + = . , ?`
- Not special: letters (`a`, `Z`), digits (`7`), and spaces

So `has_special("Hello World")` is `False`, because the only non-letter in it is a space.

## Function Signatures

Every function takes one string and returns a `bool` (`True` or `False`). **Return the answer, don't print it.** The tests compare return values.

```python
has_min_length(password: str) -> bool
has_uppercase(password: str) -> bool
has_lowercase(password: str) -> bool
has_digit(password: str) -> bool
has_special(password: str) -> bool
is_valid_password(password: str) -> bool
```

`is_valid_password` returns `True` only when **all five** helper functions return `True`.

## Examples

### `is_valid_password`

| input | output | why |
|---|---|---|
| `is_valid_password("Hello@12")` | `True` | all 5 rules pass |
| `is_valid_password("hello@12")` | `False` | no uppercase letter |
| `is_valid_password("Hi@1")` | `False` | fewer than 8 characters |
| `is_valid_password("")` | `False` | an empty password fails every rule |

## Requirements

1. Implement all five `has_*` functions.
2. Implement `is_valid_password` by **calling** those functions. Don't copy their logic into `is_valid_password`.

## Assumptions

- The password is always a string (it can be empty).
- Spaces count toward the length, but they never count as uppercase, lowercase, digit, or special.
- Functions return `bool`. Do not print.

## Hint

How would you check if *at least one* character in a string satisfies a condition?

Start with the simplest idea: loop through the characters and stop as soon as you find a match. Then see if Python has a shorter way to do the same thing.

## Bonus

Implement `get_failed_requirements(password: str) -> list[str]`.

It returns a list with the name of every rule that failed, always in this order:

`"min_length"`, `"uppercase"`, `"lowercase"`, `"digit"`, `"special"`

It returns `[]` if the password is valid.

| input | output |
|---|---|
| `get_failed_requirements("Hello@12")` | `[]` |
| `get_failed_requirements("hello@12")` | `["uppercase"]` |
| `get_failed_requirements("abc")` | `["min_length", "uppercase", "digit", "special"]` |
| `get_failed_requirements("")` | `["min_length", "uppercase", "lowercase", "digit", "special"]` |
