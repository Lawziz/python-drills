import ast
import inspect
from remove_duplicates import remove_duplicates

def uses_set(fn):
    tree = ast.parse(inspect.getsource(fn))
    return any(
        (isinstance(node, ast.Name) and node.id == "set") or isinstance(node, ast.SetComp)
        for node in ast.walk(tree)
    )

tests = [
    ([1, 2, 3, 4], [1, 2, 2, 3, 4, 4]),   # example from the problem
    ([1, 2, 3], [1, 2, 3]),               # no duplicates
    ([1], [1, 1, 1, 1]),                  # all the same
    ([], []),                             # empty
    ([3, 1, 2], [3, 1, 3, 2, 1]),         # order of first appearance, not sorted
    (["a", "b"], ["a", "b", "a"]),        # non-numbers
    ([1, 2], [1, 1, 2, 2]),               # consecutive duplicates
]

failures = 0

for expected, nums in tests:
    original = list(nums)
    got = remove_duplicates(nums)
    if got != expected:
        failures += 1
        print(f"FAIL: remove_duplicates({original})")
        print(f"  expected: {expected}")
        print(f"  got:      {got}\n")
    elif nums != original:
        failures += 1
        print(f"FAIL: remove_duplicates({original}) mutated its input\n")

if uses_set(remove_duplicates):
    failures += 1
    print("FAIL: set() is not allowed in this problem\n")

print("BIM!!!" if failures == 0 else f"{failures} failed")