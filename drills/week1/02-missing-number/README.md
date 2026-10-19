# Find the Missing Number

## Problem
Given a sorted list of consecutive integers with exactly one number missing, return the missing number.

## Function Signature
`find_missing(nums) -> int`

## Examples
| input | output | why |
|---|---|---|
| `[1, 2, 3, 5, 6]` | `4` | the list runs from 1 to 6, and 4 is the only number absent |
| `[1, 3]` | `2` | smallest valid input: the gap sits between the two items |
| `[5, 6, 8, 9]` | `7` | the list doesn't have to start at 1 |
| `[-2, -1, 1, 2]` | `0` | negatives are allowed, and the gap can be zero |

## Assumptions
- input is sorted ascending
- exactly one number is missing
- the missing number is never the first or last element (it is always between two items in the list)
- no duplicates

## Hint
look at the difference between each pair of neighbours. where is it not 1?