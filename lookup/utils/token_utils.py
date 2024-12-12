from spacy.lang.en.stop_words import STOP_WORDS
import re

def tokenize(user_input):
    user_input = user_input.lower().strip()
    user_input = re.sub(r'[^a-z0-9\s]', '', user_input)  # Removing anything that's not a lower case letter or a digit
    user_input = re.sub(r'\s{2,}', ' ', user_input)  # Replacing consecutive spaces with single space

    tokens = [token for token in user_input.split() if token not in STOP_WORDS]
    return tokens