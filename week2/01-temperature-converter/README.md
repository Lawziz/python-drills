# Temperature Converter

## Problem
Convert temperatures between Celsius, Fahrenheit and Kelvin using functions that return the result (not print it), and reject invalid input.

## Function Signatures
- `celsius_to_fahrenheit(celsius) -> float`
- `fahrenheit_to_celsius(fahrenheit) -> float`
- `celsius_to_kelvin(celsius) -> float`
- `convert_temperature(value, from_unit, to_unit) -> float`

Units are `"celsius"`, `"fahrenheit"` and `"kelvin"`.

## Examples
| input | output | why |
|---|---|---|
| `convert_temperature(0, "celsius", "fahrenheit")` | `32` | water freezes at 0C and 32F |
| `convert_temperature(-40, "celsius", "fahrenheit")` | `-40` | the two scales meet at -40 |
| `convert_temperature(100, "celsius", "kelvin")` | `373.15` | boiling point of water in Kelvin |
| `convert_temperature(25, "celsius", "celsius")` | `25` | same unit returns the original value |
| `convert_temperature(25, "rankine", "celsius")` | raises `ValueError` | unsupported unit |
| `convert_temperature(-300, "celsius", "kelvin")` | raises `ValueError` | below absolute zero |
| `convert_temperature("25", "celsius", "kelvin")` | raises `ValueError` | text is not a number |

## Assumptions
- unit names ignore case (`"Celsius"` works)
- `ValueError` is raised for unknown units, non-numbers (including numeric strings and booleans like `True`/`False`), and temperatures below absolute zero
- temperatures below absolute zero are invalid (research the standard 2-decimal constants for Celsius, Fahrenheit, and Kelvin; exactly absolute zero is allowed)
- the three helper functions do only the maths, no validation
- tests compare floats with `math.isclose`, so tiny rounding differences are fine

## Hint
Nine conversions look like a lot of formulas. What if every conversion went through one unit first?