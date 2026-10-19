# Majority Element

## Problem
Given a list of numbers, return the element that appears strictly more than half the time (more than `len(numbers) / 2`).

If no majority element exists, return `None`.

## Function Signature
`majority_element(numbers) -> int | None`

## Examples
| input | output | why |
|---|---|---|
| `[3, 2, 3]` | `3` | length is 3; threshold is 1.5; 3 appears 2 times |
| `[2, 2, 1, 1, 1, 2, 2]` | `2` | length is 7; threshold is 3.5; 2 appears 4 times |
| `[1, 1, 1, 2, 3]` | `1` | length is 5; threshold is 2.5; 1 appears 3 times |
| `[1, 2, 3, 4]` | `None` | no element appears more than 2 times |
| `[1, 2, 1, 2]` | `None` | length is 4; 1 and 2 appear exactly half the time (not strictly more than half) |
| `[5]` | `5` | single element appears once (1 > 0.5) |
| `[0, 0, 1, 0]` | `0` | 0 appears 3 times out of 4 |
| `[-1, -1, -1, 2, 3]` | `-1` | negatives are allowed; -1 appears 3 times out of 5 |
| `[]` | `None` | empty list has no majority element |

## Requirements
To complete this drill, your solution must pass both parts:
1. **Part 1 — Correctness**: return the correct majority element (or `None`) for all test cases without modifying the input list.
2. **Part 2 — Algorithmic Efficiency**:
   - **Time complexity:** $O(n)$ time. Calling `.count()` inside a loop is $O(n^2)$ and will be too slow on large lists.
   - **Space complexity:** $O(1)$ auxiliary space. Your final solution must not store counts in a dictionary, hash map, or duplicate list.

## Assumptions
- numbers can be positive, negative, or zero
- "more than half" means strictly greater than `len(numbers) / 2`. Appearing exactly half the time is not a majority (`[1, 2, 1, 2]` must return `None`)
- a list can have at most one majority element
- return `None` (not `0`, not `"None"`) when no majority exists
- do not modify the original list

## Hint
Start by solving Part 1 using a dictionary to count frequencies so you understand the problem and get the correctness tests to pass.

Once Part 1 passes, research the **Boyer–Moore Voting Algorithm** to satisfy Part 2. Research why a standard Boyer–Moore implementation needs a second verification pass when a majority element is not guaranteed to exist.
