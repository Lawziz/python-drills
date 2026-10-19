from rotate_list import rotate_list

tests = [
    ([4, 5, 1, 2, 3], [1, 2, 3, 4, 5], 2),   # example from the problem
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 0),   # k = 0
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5),   # k = len, full rotation
    ([4, 5, 1, 2, 3], [1, 2, 3, 4, 5], 7),   # k > len, same as k = 2
    ([5, 1, 2, 3, 4], [1, 2, 3, 4, 5], 1),   # k = 1
    ([1], [1], 3),                           # single element
    ([], [], 4),                             # empty list
    ([2, 1], [1, 2], 1),                     # two elements
]

failures = 0

for expected, nums, k in tests:
    original = list(nums)
    got = rotate_list(nums, k)
    if got != expected:
        failures += 1
        print(f"FAIL: rotate_list({original}, {k})")
        print(f"  expected: {expected}")
        print(f"  got:      {got}\n")

print("BIM!!!" if failures == 0 else f"{failures} failed")