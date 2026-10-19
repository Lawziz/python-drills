from count_characters import count_characters

def counts(letters, numbers, spaces, special):
    return {"letters": letters, "numbers": numbers, "spaces": spaces, "special": special}

tests = [
    (counts(10, 3, 2, 1), "Hello World 123!"),  # one of each kind
    (counts(0, 0, 0, 0), ""),                   # empty
    (counts(3, 0, 0, 0), "abc"),                # letters only
    (counts(0, 5, 0, 0), "12345"),              # each digit counts once
    (counts(0, 0, 3, 0), "   "),                # spaces only
    (counts(0, 0, 0, 5), "!@#$%"),              # special only
    (counts(2, 2, 1, 1), "a1 b2!"),             # mixed
    (counts(6, 3, 0, 1), "Python3.12"),         # '.' is special
]

failures = 0

for expected, text in tests:
    got = count_characters(text)
    if got != expected:
        failures += 1
        print(f"FAIL: count_characters({text!r})")
        print(f"  expected: {expected}")
        print(f"  got:      {got}\n")

print("BIM!!!" if failures == 0 else f"{failures} failed")