def has_min_length(password):
    return len(password) >= 8


def has_uppercase(password):
    return any(x.isupper() for x in password)  # any() stops at the first True it finds


def has_lowercase(password):
    return any(x.islower() for x in password)


def has_digit(password):
    return any(x.isdigit() for x in password)


def has_special(password):
    return any(not x.isalnum() and x != " " for x in password)  # alphanumeric and spaces don't count


def is_valid_password(password):
    return (
        has_min_length(password) and
        has_uppercase(password) and
        has_lowercase(password) and
        has_digit(password) and
        has_special(password)
    )


# bonus
def get_failed_requirements(password):
    failed = []
    if not has_min_length(password):    # order matches the spec: min_length first
        failed.append("min_length")
    if not has_uppercase(password):
        failed.append("uppercase")
    if not has_lowercase(password):
        failed.append("lowercase")
    if not has_digit(password):
        failed.append("digit")
    if not has_special(password):
        failed.append("special")
    return failed