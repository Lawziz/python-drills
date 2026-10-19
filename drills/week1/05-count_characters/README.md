# Count Characters

## Problem
Given a string, count how many letters, numbers, spaces and special characters it contains.

## Function Signature
`count_characters(text) -> dict`

returns `{"letters": ..., "numbers": ..., "spaces": ..., "special": ...}`

## Examples
| input | output | why |
|---|---|---|
| `"Hello World 123!"` | `{"letters": 10, "numbers": 3, "spaces": 2, "special": 1}` | 10 letters, digits 1-2-3, two spaces, one `!` |
| `"Python3.12"` | `{"letters": 6, "numbers": 3, "spaces": 0, "special": 1}` | `.` is not a letter, digit or space, so it is special |
| `""` | all zeros | nothing to count |

## Assumptions
- each digit counts as one number (`"12"` is 2, not one number)
- a space means `" "` only
- anything that is not a letter, digit or space is special

## Hint
check each character one at a time. which string methods tell you if a character is a letter or a digit?