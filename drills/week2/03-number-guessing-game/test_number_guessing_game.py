import io
import unittest.mock
from contextlib import redirect_stdout

from number_guessing_game import play_game

core_total = 0
core_fail = 0
bonus_total = 0
bonus_fail = 0


def check_output(label, output, expected_phrase, bonus=False):
    global core_total, core_fail, bonus_total, bonus_fail
    if bonus:
        bonus_total += 1
    else:
        core_total += 1

    if isinstance(expected_phrase, (list, tuple)):
        passed = any(p.lower() in output.lower() for p in expected_phrase)
        expected_desc = " or ".join(repr(p) for p in expected_phrase)
    else:
        passed = expected_phrase.lower() in output.lower()
        expected_desc = repr(expected_phrase)

    if not passed:
        if bonus:
            bonus_fail += 1
        else:
            core_fail += 1
        print(f"FAIL [{label}]")
        print(f"  expected to find: {expected_desc}")
        actual_clean = output.strip()
        if not actual_clean:
            print("  in actual output: <empty output>\n")
        else:
            print(f"  in actual output: {actual_clean!r}\n")


def guess_count(count):
    if count == 1:
        return ["correct! you got it in 1 guess", "correct! you got it in 1 guesses"]
    return f"correct! you got it in {count} guesses"


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
check_output("immediate correct guess", out1, guess_count(1))

out2 = run_game(["50", "37"], target=37)
check_output("feedback too high", out2, "too high")
check_output("count 2 guesses after too high", out2, guess_count(2))

out3 = run_game(["25", "37"], target=37)
check_output("feedback too low", out3, "too low")
check_output("count 2 guesses after too low", out3, guess_count(2))

# ── input validation ──────────────────────────────────────────────────────────
out4 = run_game(["hello", "37"], target=37)
check_output("invalid non-integer error", out4, "invalid")
check_output("invalid non-integer not counted", out4, guess_count(1))

out5 = run_game(["3.5", "37"], target=37)
check_output("decimal error", out5, "invalid")
check_output("decimal not counted", out5, guess_count(1))

out6 = run_game(["", "   ", "37"], target=37)
check_output("empty string not counted", out6, guess_count(1))

out7 = run_game(["0", "-5", "37"], target=37)
check_output("numbers below 1 not counted", out7, guess_count(1))

out8 = run_game(["101", "200", "37"], target=37)
check_output("numbers above 100 not counted", out8, guess_count(1))

# ── boundary and example session ──────────────────────────────────────────────
out9 = run_game(["1", "100", "50"], target=50)
check_output("1 is too low", out9, "too low")
check_output("100 is too high", out9, "too high")
check_output("boundaries 1 and 100 are valid guesses", out9, guess_count(3))

out10 = run_game(["hello", "50", "25", "37"], target=37)
check_output("example session ends in 3 guesses", out10, guess_count(3))

print(f"\ncore: {core_total - core_fail}/{core_total} passed")
if core_fail == 0:
    print("BIM!!!")

# ── bonus ─────────────────────────────────────────────────────────────────────
out_bonus1 = run_game(["10", "20", "30"], target=77, max_attempts=3)
if "77" in out_bonus1 or "game over" in out_bonus1.lower() or "attempt" in out_bonus1.lower():
    check_output("max attempts reveals number", out_bonus1, "77", bonus=True)
    print(f"\nbonus: {bonus_total - bonus_fail}/{bonus_total} passed")
else:
    print("\nbonus: skipped (max_attempts not implemented)")
