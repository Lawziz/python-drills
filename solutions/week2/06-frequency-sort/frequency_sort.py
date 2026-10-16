def frequency_sort(items):
    count = {}
    for n in items:
        count[n] = count.get(n, 0) + 1

    return sorted(items, key=lambda x: (-count[x], x))  # negate count for descending frequency; value for ascending tie-break
