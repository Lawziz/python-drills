# Matrix Row / Column Sum

## Problem
given a matrix (a list of rows), return the sum of each row and the sum of each column.

## Function Signature
`matrix_sums(matrix) -> (list, list)`

returns a tuple: `(row_sums, col_sums)`

## Examples
| input | output | why |
|---|---|---|
| `[[1, 2], [3, 4]]` | `([3, 7], [4, 6])` | rows: 1+2, 3+4. columns: 1+3, 2+4 |
| `[[1, 2, 3], [4, 5, 6]]` | `([6, 15], [5, 7, 9])` | 2 rows give 2 row sums, 3 columns give 3 column sums |
| `[[5]]` | `([5], [5])` | one cell is both a row and a column |
| `[]` | `([], [])` | no rows, nothing to sum |

## Assumptions
- every row has the same length
- the matrix may be empty (`[]`)
- return a tuple of two lists, in the order rows then columns
- return new lists, don't modify the matrix

## Hint
use a loop inside a loop. the outer loop picks a row, the inner loop visits each value in it. where can you add each value so the column total builds up as you go?