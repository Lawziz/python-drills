# Intersection of Two Lists

## Problem
Given two lists, return a new list of the elements that appear in both.

## Function Signature
`intersection(a, b) -> list`

## Examples
| input | output | why |
|---|---|---|
| `[1, 2, 3, 4]`, `[3, 4, 5, 6]` | `[3, 4]` | 3 and 4 are the only numbers in both lists |
| `[1, 2, 2, 3]`, `[2, 2, 3]` | `[2, 3]` | each common element appears once, even if repeated |
| `[3, 1, 2]`, `[1, 3]` | `[3, 1]` | the order follows the first list |
| `[1, 2]`, `[3, 4]` | `[]` | nothing in common |

## Assumptions
- the result keeps the order of the first list
- each common element appears once in the result
- return a new list, don't modify either input
- items can be numbers or strings

## Hint
go through the first list. for each item, what two things must be true before you add it to the result?