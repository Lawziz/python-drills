import ast
from pathlib import Path
import time
from longest_consecutive import longest_consecutive

part1_total = 0
part1_fail = 0
part2_total = 0
part2_fail = 0


def check(label, got, expected):
    global part1_total, part1_fail
    part1_total += 1
    if got != expected:
        part1_fail += 1
        print(f"FAIL [{label}]")
        print(f"  expected: {expected!r}")
        print(f"  got:      {got!r}\n")


def uses_sorting():
    try:
        src_file = Path(__file__).parent / "longest_consecutive.py"
        tree = ast.parse(src_file.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in ("sorted", "sort"):
                return True
            if isinstance(node, ast.Attribute) and node.attr == "sort":
                return True
        return False
    except Exception:
        return False


# ── Part 1: Correctness ────────────────────────────────────────────────────────

# examples from spec
check("spec example 1: [100, 4, 200, 1, 3, 2]",       longest_consecutive([100, 4, 200, 1, 3, 2]),       4)
check("spec example 2: sorted [1, 2, 3, 4, 5]",       longest_consecutive([1, 2, 3, 4, 5]),               5)
check("spec example 3: no consecutive [10, 30, 20]",  longest_consecutive([10, 30, 20]),                  1)
check("spec example 4: duplicates [1, 1, 2, 2, 3]",   longest_consecutive([1, 1, 2, 2, 3]),               3)
check("spec example 5: [9, 1, 4, 7, 3, 2, 6, 5]",     longest_consecutive([9, 1, 4, 7, 3, 2, 6, 5]),     7)
check("spec example 6: empty list []",                longest_consecutive([]),                            0)
check("spec example 7: negatives [-3, -2, -1, 1, 2]", longest_consecutive([-3, -2, -1, 1, 2]),            3)
check("spec example 8: single element [5]",           longest_consecutive([5]),                           1)

# edge cases
check("all identical elements [0, 0, 0, 0]",          longest_consecutive([0, 0, 0, 0]),                  1)
check("negative streak [-10, -9, -8, -7]",            longest_consecutive([-10, -9, -8, -7]),             4)
check("streak across zero [-2, -1, 0, 1, 2]",         longest_consecutive([-2, -1, 0, 1, 2]),             5)
check("reverse order [5, 4, 3, 2, 1]",                longest_consecutive([5, 4, 3, 2, 1]),               5)
check("large gaps [1, 2, 1000, 1001, 1002, 50000]",   longest_consecutive([1, 2, 1000, 1001, 1002, 50000]), 3)
check("equal length sequences [1, 2, 10, 11]",        longest_consecutive([1, 2, 10, 11]),               2)
check("unsorted duplicates [100, 4, 200, 1, 3, 2, 4, 3, 2, 1]", longest_consecutive([100, 4, 200, 1, 3, 2, 4, 3, 2, 1]), 4)

# do not mutate original list
orig = [100, 4, 200, 1, 3, 2]
orig_copy = orig.copy()
res = longest_consecutive(orig)
part1_total += 1
if orig != orig_copy:
    part1_fail += 1
    print("FAIL [does not mutate original list]")
    print(f"  original list was modified: changed from {orig_copy!r} to {orig!r}\n")

print(f"Part 1 (Correctness): {part1_total - part1_fail}/{part1_total} passed")


# ── Part 2: Algorithmic Efficiency ────────────────────────────────────────────

if part1_fail > 0:
    print("\nPart 2 (Algorithmic Efficiency): skipped (fix Part 1 correctness first)")
else:
    print("\nPart 2 (Algorithmic Efficiency):")

    # 1. Check that sorting is not used (must use O(n) set approach)
    part2_total += 1
    if uses_sorting():
        part2_fail += 1
        print("FAIL [efficiency: no-sorting constraint]")
        print("  Sorting was detected in your code (sorted() or .sort()).")
        print("  To pass Part 2, refactor to average O(n) using a set without sorting!\n")
    else:
        print("  [PASS] algorithm: no sorting detected (O(n) set approach verified)")

    # 2. Performance check: 20,000 consecutive items must complete in < 1.0s
    part2_total += 1
    large_input = list(range(20000))
    start_time = time.perf_counter()
    ans = longest_consecutive(large_input)
    elapsed = time.perf_counter() - start_time

    if ans != 20000:
        part2_fail += 1
        print("FAIL [performance: large input correctness]")
        print(f"  expected: 20000, got: {ans!r}\n")
    elif elapsed > 1.0:
        part2_fail += 1
        print("FAIL [performance: O(n) requirement]")
        print(f"  took: {elapsed:.2f}s (must finish in < 1.0s)")
        print("  Hint: make sure you only start counting when num - 1 is NOT in the set!\n")
    else:
        print(f"  [PASS] time complexity: {elapsed:.3f}s (< 1.0s, O(n) verified)")

    print(f"\nPart 2 result: {part2_total - part2_fail}/{part2_total} passed")

    if part2_fail == 0:
        print("\nBIM!!!")
    else:
        print("\nDrill incomplete: Part 2 efficiency requirements must pass to finish this drill.")
