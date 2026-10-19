from fizzbuzz import fizzbuzz

tests = [
    (["1", "2", "Fizz", "4", "Buzz"], 5),
    (["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
      "11", "Fizz", "13", "14", "FizzBuzz"], 15),   # first FizzBuzz
    (["1"], 1),                                       # minimal
    ([], 0),                                          # nothing to generate
    (["1", "2"], 2),                                  # no Fizz/Buzz at all
]

failures = 0

for expected, n in tests:
    got = fizzbuzz(n)
    if got != expected:
        failures += 1
        print(f"FAIL: fizzbuzz({n})")
        print(f"  expected: {expected}")
        print(f"  got:      {got}\n")

print("BIM!!!" if failures == 0 else f"{failures} failed")