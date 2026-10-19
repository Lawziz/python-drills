# FizzBuzz

## Problem
Given a number `n`, return a list of strings for every number from 1 to n (inclusive):
- divisible by 3 → "Fizz"
- divisible by 5 → "Buzz"
- divisible by both 3 and 5 → "FizzBuzz"
- otherwise → the number as a string

## Function Signature
`fizzbuzz(n) -> list[str]`

It must return the list, not print it. tests compare return values.

## Examples
| input | output | why |
|---|---|---|
| `fizzbuzz(5)` | `["1", "2", "Fizz", "4", "Buzz"]` | 3 is divisible by 3, 5 is divisible by 5 |
| `fizzbuzz(15)` | `[..., "FizzBuzz"]` | 15 is divisible by both 3 and 5, so the last item is "FizzBuzz" |
| `fizzbuzz(1)` | `["1"]` | 1 is divisible by neither |
| `fizzbuzz(0)` | `[]` | no numbers between 1 and 0 |

## Assumptions
- range is 1 to n inclusive
- n is a non-negative integer
- numbers are returned as strings, so the whole list has one type

## Hint
think about the order of your checks. what happens to 15 if you test divisibility by 3 first?
