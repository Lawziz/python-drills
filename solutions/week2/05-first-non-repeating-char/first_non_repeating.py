def first_non_repeating(s, case_sensitive=True):
    text = s if case_sensitive else s.lower()   # normalise once so every lookup is consistent
    count = {}
    for ch in text:
        count[ch] = count.get(ch, 0) + 1

    for i, ch in enumerate(text):              # iterate with index to return the original-case character
        if count[ch] == 1:
            return s[i]                        # s[i] preserves the original case even when case_sensitive=False

    return None
