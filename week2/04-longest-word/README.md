# Longest Word

## Problem
Given a sentence, return the longest word. If two words tie, return the first one encountered.

## Function Signature
`longest_word(sentence) -> str`

## Examples
| input | output | why |
|---|---|---|
| `"the quick brown fox"` | `"quick"` | 5 chars, longest |
| `"hi there"` | `"there"` | `"there"` is 5 chars, `"hi"` is 2 chars |
| `"cat bat rat"` | `"cat"` | all 3 chars — first encountered wins |
| `"hello, world"` | `"hello"` | punctuation stripped before measuring |
| `""` | `""` | empty input, empty output |

## Assumptions
- split on whitespace to get tokens
- strip leading and trailing punctuation from each token before measuring (`"hello,"` → `"hello"`)
- ties go to the **first** word encountered
- empty string → return `""`
- a token that becomes empty after stripping (e.g. `"---"`) is ignored

## Hint
How would you remove characters from just the beginning and end of a string in Python?

## Bonus
`longest_words(sentence) -> list[str]`

Return all words tied for the longest length as a list, preserving their original order of appearance. Return `[]` if there are no words.

```python
longest_words("cat bat rat")          # → ["cat", "bat", "rat"]
longest_words("the quick brown fox")  # → ["quick", "brown"]
```
