# utils.py
# A simple utility file with three beginner-friendly functions.


def is_palindrome(s):
    """
    Check whether a string is a palindrome.

    A palindrome reads the same forwards and backwards (e.g., "madam").
    This function ignores uppercase/lowercase differences and spaces.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, otherwise False.
    """
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_words(text):
    """
    Count the number of words in a given text.

    Words are separated by spaces.

    Parameters:
        text (str): The text in which to count words.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)


def celsius_to_fahrenheit(c):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Formula: F = (C * 9/5) + 32

    Parameters:
        c (int or float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (c * 9 / 5) + 32