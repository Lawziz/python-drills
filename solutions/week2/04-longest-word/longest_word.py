import string


def longest_word(sentence):
    words = [
        word.strip(string.punctuation)
        for word in sentence.split()
        if word.strip(string.punctuation)   # skip tokens that become empty after stripping (e.g. "---")
    ]

    max_len = 0
    longest = ""
    for word in words:
        if len(word) > max_len:             # strict >, so a tie keeps the first occurrence
            max_len, longest = len(word), word
    return longest


# bonus
def longest_words(sentence):
    words = [
        word.strip(string.punctuation)
        for word in sentence.split()
        if word.strip(string.punctuation)
    ]

    if not words:
        return []

    max_len = max(len(w) for w in words)    # find the target length first
    return [w for w in words if len(w) == max_len]  # collect every word that matches it
