#!/usr/bin/python3
def multiple_returns(sentence):
    """Return length of a string and its first letter in a tuple"""

    if type(sentence) is str and sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
