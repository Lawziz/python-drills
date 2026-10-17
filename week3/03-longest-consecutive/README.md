# Longest Consecutive Sequence

## Problem
Given a list of numbers, return the length of the longest sequence of consecutive integers.

The numbers do not need to appear next to each other in the original list.

## Function Signature
`longest_consecutive(numbers) -> int`

## Examples
| input | output | why |
|---|---|---|
| `[100, 4, 200, 1, 3, 2]` | `4` | the sequence `1, 2, 3, 4` has length 4 |
| `[1, 2, 3, 4, 5]` | `5` | the entire list forms a consecutive sequence |
| `[10, 30, 20]` | `1` | no two numbers are consecutive; longest streak is 1 |
| `[1, 1, 2, 2, 3]` | `3` | duplicates count once; sequence is `1, 2, 3` |
| `[9, 1, 4, 7, 3, 2, 6, 5]` | `7` | sequence is `1, 2, 3, 4, 5, 6, 7` |
| `[-3, -2, -1, 1, 2]` | `3` | sequence is `-3, -2, -1` (0 is missing to connect to 1, 2) |
| `[5]` | `1` | single element has streak length 1 |
| `[]` | `0` | empty list has streak length 0 |

## Requirements
To complete this drill, your solution must pass both parts:
1. **Part 1 — Correctness**:
   - return the length of the longest consecutive sequence
   - return `0` if the list is empty
   - do not count duplicate numbers more than once
   - do not modify the original list
2. **Part 2 — Algorithmic Efficiency**:
   - **Time complexity:** average $O(n)$ time.
   - **Constraint:** do not sort the list (`sorted` and `.sort()` are `O(n log n)`). Achieve average $O(n)$ time using a set lookup approach.

## Assumptions
- numbers are integers (positive, negative, or zero)
- original order does not matter
- empty list returns `0`
- do not mutate the input list

## Hint
Start by solving Part 1 using sorting (`sorted()`) to understand the problem and get all test cases to pass.

Once Part 1 passes, refactor for Part 2 using a **set** to get $O(n)$ time without sorting:
- Inserting all numbers into a `set` gives $O(1)$ average lookups.
- *The key efficiency insight:* When iterating through your set, how do you know if a number is the **beginning** of a streak? If `num - 1` is already in the set, should you start counting from `num`, or skip it and let its streak be counted from its true beginning?
