import time
import tracemalloc
from majority_element import majority_element

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


# ── Part 1: Correctness ────────────────────────────────────────────────────────

# examples from spec
check("spec example 1: [3, 2, 3]",                   majority_element([3, 2, 3]),                   3)
check("spec example 2: [2, 2, 1, 1, 1, 2, 2]",       majority_element([2, 2, 1, 1, 1, 2, 2]),       2)
check("spec example 3: [1, 1, 1, 2, 3]",             majority_element([1, 1, 1, 2, 3]),             1)
check("spec example 4: [1, 2, 3, 4]",                majority_element([1, 2, 3, 4]),                None)
check("spec example 5: single element [5]",          majority_element([5]),                          5)
check("spec example 6: zeros [0, 0, 1, 0]",          majority_element([0, 0, 1, 0]),                0)
check("spec example 7: negatives [-1, -1, -1, 2, 3]",majority_element([-1, -1, -1, 2, 3]),         -1)
check("spec example 8: empty list []",               majority_element([]),                          None)
check("spec example 9: exactly half [1, 2, 1, 2]",   majority_element([1, 2, 1, 2]),                None)

# edge cases
check("single negative element",                     majority_element([-99]),                       -99)
check("single zero",                                 majority_element([0]),                         0)
check("all identical elements",                      majority_element([7, 7, 7, 7]),                7)
check("all unique elements",                         majority_element([10, 20, 30, 40, 50]),        None)
check("several equal frequencies (no majority)",     majority_element([1, 1, 2, 2, 3, 3]),          None)
check("negative majority with zeros",                majority_element([-5, -5, 0, -5]),             -5)
check("majority at the beginning",                   majority_element([4, 4, 4, 1, 2]),             4)
check("majority at the end",                         majority_element([1, 2, 4, 4, 4]),             4)
check("exactly half (even length tie)",              majority_element([6, 6, 7, 8]),                None)
check("no majority (candidate trap 1)",              majority_element([1, 2, 3]),                   None)
check("no majority (candidate trap 2)",              majority_element([2, 1, 2, 3, 1]),             None)
check("interleaved majority",                        majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4]), 4)

# do not mutate original list
orig = [3, 2, 3]
orig_copy = orig.copy()
res = majority_element(orig)
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
    
    # 1. Time complexity check: 100k items must complete in < 1.0s
    part2_total += 1
    large_list = [42] * 50001 + [1] * 49999
    start_time = time.perf_counter()
    ans_time = majority_element(large_list)
    elapsed = time.perf_counter() - start_time
    
    if ans_time != 42:
        part2_fail += 1
        print("FAIL [time: large list correctness]")
        print(f"  expected: 42, got: {ans_time!r}\n")
    elif elapsed > 1.0:
        part2_fail += 1
        print("FAIL [time: O(n) requirement]")
        print(f"  took: {elapsed:.2f}s (must finish in < 1.0s; avoid O(n^2) nested loops or .count())\n")
    else:
        print(f"  [PASS] time complexity: {elapsed:.3f}s (< 1.0s, O(n) verified)")

    # 2. Space complexity check: must use O(1) auxiliary space (< 50 KB peak allocation)
    part2_total += 1
    # 50,000 distinct values + 50,001 majority values
    stress_data = list(range(50000)) + [999999] * 50001
    
    tracemalloc.start()
    ans_space = majority_element(stress_data)
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    peak_kb = peak_bytes / 1024
    if ans_space != 999999:
        part2_fail += 1
        print("FAIL [space: stress test correctness]")
        print(f"  expected: 999999, got: {ans_space!r}\n")
    elif peak_bytes > 50 * 1024:
        part2_fail += 1
        print("FAIL [space: O(1) auxiliary space requirement]")
        print(f"  peak memory allocated: {peak_kb:.1f} KB (limit: 50.0 KB)")
        print("  A dictionary/hash map was detected. Refactor to O(1) space using the Boyer–Moore Voting Algorithm!\n")
    else:
        print(f"  [PASS] space complexity: {peak_kb:.1f} KB (< 50.0 KB, O(1) auxiliary space verified)")

    print(f"\nPart 2 result: {part2_total - part2_fail}/{part2_total} passed")

    if part2_fail == 0:
        print("\nBIM!!!")
    else:
        print("\nDrill incomplete: Part 2 efficiency requirements must pass to finish this drill.")
