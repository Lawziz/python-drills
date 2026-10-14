from matrix_sums import matrix_sums

tests = [
    (([3, 7], [4, 6]), [[1, 2], [3, 4]]),                       # 2x2, rows and cols differ
    (([6, 15], [5, 7, 9]), [[1, 2, 3], [4, 5, 6]]),             # 2 rows x 3 cols
    (([3, 7, 11], [9, 12]), [[1, 2], [3, 4], [5, 6]]),          # 3 rows x 2 cols
    (([6, 15, 24], [12, 15, 18]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # 3x3
    (([6], [1, 2, 3]), [[1, 2, 3]]),                            # one row
    (([1, 2, 3], [6]), [[1], [2], [3]]),                        # one column
    (([5], [5]), [[5]]),                                        # single cell
    (([0, 0], [-1, 1]), [[-1, 1], [0, 0]]),                     # negatives and zeros
    (([0, 0], [0, 0]), [[0, 0], [0, 0]]),                       # all zeros
    (([], []), []),                                             # empty matrix
]

failures = 0

for expected, matrix in tests:
    before = [row[:] for row in matrix]
    got = matrix_sums(matrix)
    if got != expected:
        failures += 1
        print(f"FAIL: matrix_sums({before})")
        print(f"  expected: {expected}")
        print(f"  got:      {got}\n")
    elif matrix != before:
        failures += 1
        print(f"FAIL: matrix_sums({before}) mutated its input\n")

print("BIM!!!" if failures == 0 else f"{failures} failed")