import io
import unittest.mock
from contextlib import redirect_stdout

from number_guessing_game import play_game

core_total = 0
core_fail = 0
bonus_total = 0
bonus_fail = 0


def check(label, got, expected, bonus=False):
    global core_total, core_fail, bonus_total, bonus_fail
    if bonus:
        bonus_total += 1
        if got != expected:
            bonus_fail += 1
            print(f"FAIL [{label}]")
            print(f"  expected: {expected!r}")
            print(f"  got:      {got!r}\n")
    else:
        core_total += 1
        if got != expected:
            core_fail += 1
            print(f"FAIL [{label}]")
            print(f"  expected: {expected!r}")
            print(f"  got:      {got!r}\n")


def got_in(output, count):
    out = output.lower()
    if count == 1:
        return "correct! you got it in 1 guess" in out or "correct! you got it in 1 guesses" in out
    return f"correct! you got it in {count} guesses" in out


def run_game(inputs, target=37, max_attempts=None):
    it = iter(inputs)
    eof_count = 0

    def mock_input(prompt=""):
        nonlocal eof_count
        try:
            return next(it)
        except StopIteration:
            eof_count += 1
            if eof_count > 10:
                # Prevent infinite loop if student's code catches EOFError inside a loop
                raise SystemExit("Loop did not terminate after inputs were exhausted")
            raise EOFError("No more mock inputs provided")

    captured = io.StringIO()
    with redirect_stdout(captured):
        with unittest.mock.patch("builtins.input", side_effect=mock_input):
            with unittest.mock.patch("random.randint", return_value=target):
                with unittest.mock.patch("random.randrange", return_value=target):
                    try:
                        if max_attempts is not None:
                            play_game(target=target, max_attempts=max_attempts)
                        else:
                            play_game(target=target)
                    except TypeError:
                        if max_attempts is not None:
                            try:
                                play_game(target=target)
                            except TypeError:
                                play_game()
                        else:
                            play_game()
                    except (EOFError, SystemExit):
                        pass
    return captured.getvalue()


# ── core gameplay ─────────────────────────────────────────────────────────────
out1 = run_game(["37"], target=37)
check("immediate correct guess", got_in(out1, 1), True)

out2 = run_game(["50", "37"], target=37)
check("feedback too high", "too high" in out2.lower(), True)
check("count 2 guesses after too high", got_in(out2, 2), True)

out3 = run_game(["25", "37"], target=37)
check("feedback too low", "too low" in out3.lower(), True)
check("count 2 guesses after too low", got_in(out3, 2), True)

# ── input validation ──────────────────────────────────────────────────────────
out4 = run_game(["hello", "37"], target=37)
check("invalid non-integer error", "invalid" in out4.lower(), True)
check("invalid non-integer not counted", got_in(out4, 1), True)

out5 = run_game(["3.5", "37"], target=37)
check("decimal error", "invalid" in out5.lower(), True)
check("decimal not counted", got_in(out5, 1), True)

out6 = run_game(["", "   ", "37"], target=37)
check("empty string not counted", got_in(out6, 1), True)

out7 = run_game(["0", "-5", "37"], target=37)
check("numbers below 1 not counted", got_in(out7, 1), True)

out8 = run_game(["101", "200", "37"], target=37)
check("numbers above 100 not counted", got_in(out8, 1), True)

# ── boundary and example session ──────────────────────────────────────────────
out9 = run_game(["1", "100", "50"], target=50)
check("1 is too low", "too low" in out9.lower(), True)
check("100 is too high", "too high" in out9.lower(), True)
check("boundaries 1 and 100 are valid guesses", got_in(out9, 3), True)

out10 = run_game(["hello", "50", "25", "37"], target=37)
check("example session ends in 3 guesses", got_in(out10, 3), True)

print(f"\ncore: {core_total - core_fail}/{core_total} passed")
if core_fail == 0:
    print("BIM!!!")

# ── bonus ─────────────────────────────────────────────────────────────────────
out_bonus1 = run_game(["10", "20", "30"], target=77, max_attempts=3)
if "77" in out_bonus1 or "game over" in out_bonus1.lower() or "attempt" in out_bonus1.lower():
    check("max attempts reveals number", "77" in out_bonus1, True, bonus=True)
    print(f"\nbonus: {bonus_total - bonus_fail}/{bonus_total} passed")
else:
    print("\nbonus: skipped (max_attempts not implemented)")
