"""
Module for tokenizing text.
"""


import string
import logging

#Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_text(text):
    """
    Convert text to lowercase and remove punctuation.

    Args:
        text (str): The input string.

    Returns:
        str: The cleaned text.
    """
    logger.info("cleaning text input...")
    assert isinstance(text, str), "Input should be a string"

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def tokenize(text):
    """
    Tokenize the input text into a list of words.

    Args:
        text (str): The input string.

    Returns:
        list: A list of words.
    """

    logger.info("tokenizing text input...")
    assert isinstance(text, str), "Input should be a string"

    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    return words

def count_words(text):
    """
    Count the frequency of each word in the text.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """

    logger.info("Counting words...")
    assert isinstance(text, str), "Input should be a string"

    words = tokenize(text)
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
