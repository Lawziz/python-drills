# Most Frequent Element

## Problem
Given a list, return the element that appears most often.

constraint: do not use `max()`.

## Function Signature
`most_frequent(items) -> element`

## examples
| input | output | why |
|---|---|---|
| `[1, 2, 2, 3]` | `2` | 2 appears twice, the others once |
| `[1, 2, 2, 1]` | `1` | tie: 1 and 2 both appear twice, 1 appeared first |
| `[]` | `None` | nothing to return |

## Assumptions
- on a tie, return the element that appears first in the list
- an empty list returns `None`
- items are hashable (numbers or strings)

## Hint
count each item first. then how do you find the biggest count without `max()`?