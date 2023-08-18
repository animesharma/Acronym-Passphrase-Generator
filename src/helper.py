def filter_short_words(words: list, min_word_len: int = 5) -> list:
    """
    Filters a list of words by removing words with length less than the specified minimum word length.

    Input Parameters:
    - words: A list of words to be filtered.
    - min_word_len: The minimum word length to keep in the filtered list, defaults to 5.

    Returns: A new list containing only the words with length greater than or equal to the specified minimum word length.
    """
    return [word for word in words if len(word) >= min_word_len]

def generate_alphabetical_dict(words: list) -> dict:
    """
    Generates a dictionary where the keys are the first letters of the words in the input list and the values are lists of words starting with that letter.
    
    Input Parameters:
    - words: A list of words to be used to generate the dictionary.
    
    Returns: A dictionary where the keys are the first letters of the words in the input list and the values are lists of words starting with that letter.
    """
    alphabetical_dict = {}
    for word in words:
        initial = word[0]
        alphabetical_dict[initial] = alphabetical_dict.get(initial, []) + [word]
    return alphabetical_dict
