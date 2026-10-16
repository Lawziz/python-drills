ABSOLUTE_ZERO = {           # minimum valid temperature for each unit
    "kelvin": 0,
    "celsius": -273.15,
    "fahrenheit": -459.67
}


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def convert_temperature(value, from_unit, to_unit):
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise ValueError("unit must be strings")
    from_unit, to_unit = from_unit.lower(), to_unit.lower()
    if from_unit not in ABSOLUTE_ZERO or to_unit not in ABSOLUTE_ZERO:
        raise ValueError("unsupported unit")
    if not isinstance(value, (int, float)) or isinstance(value, bool):  # bool is a subclass of int, so it must be excluded explicitly
        raise ValueError("value should be a number")
    if value < ABSOLUTE_ZERO[from_unit]:
        raise ValueError("below absolute zero")

    if from_unit == to_unit:        # same unit: nothing to convert
        return value

    # convert anything to celsius first, then celsius to the target unit
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = fahrenheit_to_celsius(value)
    else:
        celsius = value - 273.15    # kelvin to celsius

    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return celsius_to_fahrenheit(celsius)
    else:
        return celsius_to_kelvin(celsius)
