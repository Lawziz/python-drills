# Move All Zeros to the End

## Problem
Given a list of numbers, move every zero to the end of the list in-place while preserving the relative order of all non-zero numbers.

## Function Signature
`move_zeros(numbers) -> list`

Modify the list in-place and return it.

## Examples
| input | output | why |
|---|---|---|
| `[0, 1, 0, 3, 12]` | `[1, 3, 12, 0, 0]` | 1, 3, 12 keep their original order; zeros move to the end |
| `[1, 2, 3]` | `[1, 2, 3]` | no zeros to move |
| `[0, 0, 0]` | `[0, 0, 0]` | all elements are zero |
| `[1, 0, 2, 0, 3]` | `[1, 2, 3, 0, 0]` | non-zeros 1, 2, 3 stay in order |
| `[4, 0, 5, 0, 0]` | `[4, 5, 0, 0, 0]` | consecutive zeros at the end |
| `[]` | `[]` | empty list |
| `[0]` | `[0]` | single zero |

## Requirements
To complete this drill, your solution must pass both parts:
1. **Part 1 — Correctness**:
   - move all zeros to the end while keeping the relative order of non-zero elements
   - preserve every element in the list (same length and counts)
   - modify the list in-place (do not return a new list object)
2. **Part 2 — Algorithmic Efficiency**:
   - **Time complexity:** $O(n)$ time. Calling `.remove()` or `.pop()` inside a loop shifts elements in $O(n)$ time on each removal, resulting in an $O(n^2)$ runtime that will time out on large lists.
   - **Space complexity:** $O(1)$ auxiliary space. Do not allocate a second list or slice copies.

## Assumptions
- numbers are integers (positive, negative, or zero)
- modify `numbers` in-place and return it (the test verifies the original list object was modified)
- relative order of non-zero elements must remain unchanged
- empty list returns `[]`

## Hint
Think about using the **two-pointer technique**:
- What if one pointer keeps track of where the next non-zero number should go?
- What if a second pointer scans through the list looking for non-zero numbers?
- How can swapping elements let you move all zeros in a single pass without extra memory?
