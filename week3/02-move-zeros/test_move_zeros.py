import time
import tracemalloc
from move_zeros import move_zeros

part1_total = 0
part1_fail = 0
part2_total = 0
part2_fail = 0


def check(label, input_list, expected):
    global part1_total, part1_fail
    part1_total += 1
    input_copy = input_list.copy()
    res = move_zeros(input_list)
    got = input_list if res is None else res

    if input_list != expected:
        part1_fail += 1
        print(f"FAIL [{label}]")
        print(f"  input:    {input_copy!r}")
        print(f"  expected: {expected!r}")
        print(f"  got:      {input_list!r}\n")
    elif res is not None and res is not input_list:
        part1_fail += 1
        print(f"FAIL [{label} - in-place modification]")
        print("  expected: modify and return the same list object")
        print("  got:      returned a new list object (do not create a second list)\n")


# ── Part 1: Correctness ────────────────────────────────────────────────────────

# examples from spec
check("spec example 1: [0, 1, 0, 3, 12]",       [0, 1, 0, 3, 12],                [1, 3, 12, 0, 0])
check("spec example 2: no zeros [1, 2, 3]",      [1, 2, 3],                       [1, 2, 3])
check("spec example 3: only zeros [0, 0, 0]",    [0, 0, 0],                       [0, 0, 0])
check("spec example 4: [1, 0, 2, 0, 3]",         [1, 0, 2, 0, 3],                 [1, 2, 3, 0, 0])
check("spec example 5: [4, 0, 5, 0, 0]",         [4, 0, 5, 0, 0],                 [4, 5, 0, 0, 0])
check("spec example 6: empty list []",           [],                              [])
check("spec example 7: single zero [0]",         [0],                             [0])

# edge cases
check("single non-zero element [5]",             [5],                             [5])
check("zeros at the beginning [0, 0, 1]",        [0, 0, 1],                       [1, 0, 0])
check("zero at the end [1, 2, 0]",               [1, 2, 0],                       [1, 2, 0])
check("consecutive zeros in middle",             [0, 0, 0, 1, 0, 0, 2, 0],        [1, 2, 0, 0, 0, 0, 0, 0])
check("negative numbers mixed with zeros",       [-1, 0, -3, 0],                  [-1, -3, 0, 0])
check("repeated non-zero numbers",               [2, 2, 0, 2, 0, 2],              [2, 2, 2, 2, 0, 0])
check("alternating clusters",                    [0, 1, 0, 0, 0, 2, 3, 0, 4],     [1, 2, 3, 4, 0, 0, 0, 0, 0])

# in-place modification identity check
tracker = [0, 1, 0, 3]
tracker_id = id(tracker)
returned = move_zeros(tracker)
part1_total += 1
if tracker != [1, 3, 0, 0]:
    part1_fail += 1
    print("FAIL [in-place modification]")
    print(f"  expected tracker list to become [1, 3, 0, 0], got: {tracker!r}\n")
elif returned is not None and id(returned) != tracker_id:
    part1_fail += 1
    print("FAIL [in-place modification identity]")
    print("  expected the function to modify the input list in-place")
    print("  got a newly allocated list object\n")

print(f"Part 1 (Correctness): {part1_total - part1_fail}/{part1_total} passed")


# ── Part 2: Algorithmic Efficiency ────────────────────────────────────────────

if part1_fail > 0:
    print("\nPart 2 (Algorithmic Efficiency): skipped (fix Part 1 correctness first)")
else:
    print("\nPart 2 (Algorithmic Efficiency):")
    
    # 1. Time complexity check: 50,000 items must finish in < 1.0s
    part2_total += 1
    large_input = [0, 1] * 25000
    expected_large = [1] * 25000 + [0] * 25000
    
    start_time = time.perf_counter()
    move_zeros(large_input)
    elapsed = time.perf_counter() - start_time
    
    if large_input != expected_large:
        part2_fail += 1
        print("FAIL [time: large list correctness]")
        print("  large list was not properly sorted with zeros at the end\n")
    elif elapsed > 1.0:
        part2_fail += 1
        print("FAIL [time: O(n) requirement]")
        print(f"  took: {elapsed:.2f}s (must finish in < 1.0s; avoid O(n^2) operations like .remove(0))\n")
    else:
        print(f"  [PASS] time complexity: {elapsed:.3f}s (< 1.0s, O(n) verified)")

    # 2. Space complexity check: O(1) auxiliary space (< 50 KB peak allocation)
    part2_total += 1
    stress_data = [0, 1] * 25000
    
    tracemalloc.start()
    move_zeros(stress_data)
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    peak_kb = peak_bytes / 1024
    if peak_bytes > 50 * 1024:
        part2_fail += 1
        print("FAIL [space: O(1) auxiliary space requirement]")
        print(f"  peak memory allocated: {peak_kb:.1f} KB (limit: 50.0 KB)")
        print("  A second list or slice was created. Solve in-place using two pointers for O(1) space!\n")
    else:
        print(f"  [PASS] space complexity: {peak_kb:.1f} KB (< 50.0 KB, O(1) auxiliary space verified)")

    print(f"\nPart 2 result: {part2_total - part2_fail}/{part2_total} passed")

    if part2_fail == 0:
        print("\nBIM!!!")
    else:
        print("\nDrill incomplete: Part 2 efficiency requirements must pass to finish this drill.")
