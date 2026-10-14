import string

def cleaned_word(token: str) -> str:
    return token.strip(string.punctuation)

# def cleaned2(token) :
#     return any(char.isalnum() for char in token if not char.isspace())

def longest_word(sentence):
    # Write your code here
    tokens = sentence.split()

    longest = ""

    for token in tokens:
        cleaned = cleaned_word(token)

        if not cleaned:
            continue
        if len(cleaned) > len(longest):
            longest = cleaned

    return longest
# bonus
def longest_words(sentence):
    # Write your code here
    tokens = sentence.split()
    # for token in tokens:
    #     cleaned = cleaned_word(token)
    cleaned = [cleaned_word(token) for token in tokens if cleaned_word(token)]
    if not cleaned:
        return []
        
    max_length = max([len(word) for word in cleaned])
    return [word for word in cleaned if len(word) == max_length]

print(longest_words("the quick brown fox"))