# First Non-Repeating Character

## Problem
Given a string, return the first character that appears exactly once. If no such character exists, return `None`.

## Function Signature
`first_non_repeating(s, case_sensitive=True) -> str | None`

## Examples
| input | output | why |
|---|---|---|
| `"aabbcde"` | `"c"` | `a` and `b` repeat; `c` is first with frequency 1 |
| `"aabb"` | `None` | every character repeats |
| `"z"` | `"z"` | only one character, appears once |
| `"aAbBc"` | `"a"` | `'a'` and `'A'` are different characters; `'a'` appears once |
| `""` | `None` | empty string |

### With `case_sensitive=False`
| input | output | why |
|---|---|---|
| `"aAbBc"` | `"c"` | counted as `"aabbc"`: `a` ×2, `b` ×2, `c` ×1 |
| `"sTreSS"` | `"T"` | counted as `"stress"`: first unique is `t`, but the input has `'T'`, so return `"T"` |
| `"Aa"` | `None` | counted as `"aa"`: the letter repeats |

## Assumptions
- case-sensitive by default (`case_sensitive=True`): `'A'` and `'a'` are treated as different characters
- when `case_sensitive=False`, case is ignored **only for counting**: `'A'` and `'a'` count as the same character
- the returned character is always **exactly as it appears in the original string**, never a lowercased version (`"sTreSS"` returns `"T"`, not `"t"`)
- return the first non-repeating character by **position in the original string**, not alphabetically
- return `None` (not `""`, not `"None"`) when none exists

## Hint
What data structure lets you count how many times each character appears in one pass?

## Bonus
- support case-insensitive matching when `case_sensitive=False` is passed (e.g. `first_non_repeating("aAbBc", case_sensitive=False) -> "c"`)
- if a character is unique under case-insensitive counting, return it in its original case from the string
