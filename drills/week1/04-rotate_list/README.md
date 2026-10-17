# Rotate List

## Problem
Given a list and a number `k`, rotate the list to the right by `k` positions.

## Function Signature
`rotate_list(nums, k) -> list`

## Examples
| input | output | why |
|---|---|---|
| `[1, 2, 3, 4, 5], k=2` | `[4, 5, 1, 2, 3]` | the last 2 items move to the front |
| `[1, 2, 3, 4, 5], k=5` | `[1, 2, 3, 4, 5]` | rotating by the full length returns the same list |
| `[1, 2, 3, 4, 5], k=7` | `[4, 5, 1, 2, 3]` | 7 is the same as 2 after one full rotation |
| `[], k=3` | `[]` | nothing to rotate |

## Assumptions
- rotation is to the right
- k is a non-negative integer, and may be larger than the list length
- return a new list

## Hint
what happens to k when it's bigger than the list? which operator wraps a number back into a range? you used it in caesar cipher.