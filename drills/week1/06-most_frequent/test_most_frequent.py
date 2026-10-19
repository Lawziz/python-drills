# test_most_frequent.py
import ast
import inspect

from most_frequent import most_frequent


def uses_name(fn, name):
    tree = ast.parse(inspect.getsource(fn))
    return any(isinstance(node, ast.Name) and node.id == name for node in ast.walk(tree))


# tie -> the element that appears first in the list
tests = [
    (2, [1, 2, 2, 3]),            # basic
    (1, [1]),                     # single element
    ("a", ["a", "b", "a"]),       # strings
    (3, [1, 2, 3, 3, 3, 2]),      # winner is not first
    (1, [1, 2, 2, 1]),            # tie, first appearance wins
    (3, [3, 4, 4, 3, 5]),         # tie between 3 and 4, 3 appears first
    (None, []),                   # empty
    (-1, [-1, -1, 2]),            # negatives
    (5, [5, 5, 5]),               # all the same
]

failures = 0

for expected, items in tests:
    got = most_frequent(items)
    if got != expected:
        failures += 1
        print(f"FAIL: most_frequent({items})")
        print(f"  expected: {expected}")
        print(f"  got:      {got}\n")

if uses_name(most_frequent, "max"):
    failures += 1
    print("FAIL: max() is not allowed in this problem\n")

print("BIM!!!" if failures == 0 else f"{failures} failed")